# AI-Ecommerce-Data-Assistant

## 💡 Gemini LLM + PostgreSQL: Intelligent SQL Assistant with Visualizations

An intelligent web-based data assistant that leverages **Google Gemini 2.5 Pro**, **FastAPI**, and **PostgreSQL** to translate natural language questions into SQL queries, fetch data, and return **interactive visualizations** using **Plotly.js**.

---

## 🧠 Features

- Natural language to SQL conversion using Gemini 2.5 Pro
- PostgreSQL query execution with schema-aware prompting
- Schema-grounded SQL generation logic
- Interactive web UI displaying SQL + tabular data + visual charts
- Plotly.js visualizations: bar charts and time trendlines
- Typing animation effect for SQL display
- Input lock during generation to prevent spamming

---

## 🏗️ Project Structure

- `main.py` — FastAPI backend server
- `llm_gemini.py` — Gemini API integration & SQL generation logic
- `sql_executor.py` — Executes generated SQL queries
- `.env` — Environment config (API keys, DB credentials)
- `requirements.txt` — Python dependencies
- `templates/index.html` — Frontend (UI + JS + Plotly)
- `README.md` — You are here

---

## ⚙️ Setup Instructions

1. Clone this repository and navigate into it  
   Repository URL: `https://github.com/your-username/gemini-sql-assistant.git`

2. Create a virtual environment using Python and activate it

3. Install all dependencies listed in `requirements.txt`

4. Create a `.env` file in the project root with the following variables:
   - `GEMINI_API_KEY`: Your Google Gemini Pro API key
   - `DB_HOST`: Your PostgreSQL host (usually `localhost`)
   - `DB_NAME`: Your PostgreSQL database name
   - `DB_USER`: Your PostgreSQL username
   - `DB_PASSWORD`: Your PostgreSQL password
   - `DB_PORT`: Usually `5432`

---

## 🚀 Running the App

Start the FastAPI server using Uvicorn.  
Once started, you can access the app at `http://localhost:8000`  
Swagger documentation is available at `http://localhost:8000/docs`

---

## 🌐 Web Interface Overview

- Accepts natural language queries from the user
- Generates the corresponding SQL query
- Displays:
  - The SQL with a typing animation
  - Tabular query results
  - Visualizations (if applicable)

### Chart Rendering Logic

- Visualizations are shown when data includes groupings (e.g., per item or date)
- No charts are displayed for simple aggregate metrics (like total sales)

---

## 🧪 Example Prompts

| User Prompt                   | Output Type                        |
|------------------------------|-------------------------------------|
| Show RoAS per item           | SQL + Table + Bar Chart             |
| Trend of ad spend over time  | SQL + Table + Line Chart            |
| Total units sold last 7 days | SQL + Table Only                    |

---

## 🧰 Tech Stack

- **Gemini 2.5 Pro** — Natural language processing
- **FastAPI** — Backend framework
- **PostgreSQL** — Database engine
- **Plotly.js** — Interactive charts
- **HTML, CSS, JavaScript** — Frontend

---

## 👨‍💻 Author

**T. Pothan Sai**  
Email: pothansaithummala@gmail.com  
LinkedIn: [linkedin.com/in/pothansai0408](https://www.linkedin.com/in/pothansai0408)  
GitHub: [PothanSai2004](https://github.com/PothanSai2004)

---
