from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from llm_gemini import generate_sql_from_question
from sql_executor import run_sql

import webbrowser
import threading
import os

app = FastAPI(
    title="E-commerce Data Agent",
    description="Ask questions to Gemini LLM and query PostgreSQL",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="templates"), name="static")

class Question(BaseModel):
    question: str

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    """Serve the HTML UI"""
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.post("/ask")
def ask_question(question: Question):
    sql = generate_sql_from_question(question.question)
    print("[Generated SQL]", sql)

    results = run_sql(sql)

    if isinstance(results, dict) and "error" in results:
        return results

    return {
        "question": question.question,
        "sql": sql,
        "results": results
    }

def open_browser():
    webbrowser.open("http://localhost:8000")

if __name__ == "__main__":
    import uvicorn
    threading.Timer(1.5, open_browser).start()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
