# AI-Ecommerce-Data-Assistant
## 💡 Gemini LLM + PostgreSQL: Intelligent SQL Assistant with Visualizations

An intelligent web-based data assistant that leverages **Google Gemini 2.5 Pro**, **FastAPI**, and **PostgreSQL** to translate natural language questions into SQL queries, fetch data, and return **interactive visualizations** using **Plotly.js**.

---

## 🧠 Features

- ✅ **Natural Language to SQL** using Google Gemini 2.5 Pro
- ✅ **PostgreSQL Query Execution** with data integrity
- ✅ **LLM-aware Prompt Engineering** with schema grounding
- ✅ **Interactive Web UI** with results, generated SQL, and charts
- ✅ **Bar Charts / Trendlines** via Plotly.js
- ✅ **Typing Animation for SQL display**
- ✅ **Input/Submit control** during response generation

---

## 🏗️ Project Structure
.
├── main.py # FastAPI backend
├── llm_gemini.py # Gemini prompt + SQL generation logic
├── sql_executor.py # Executes generated SQL against PostgreSQL
├── .env # Environment config (API keys, DB creds)
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend UI (HTML + Plotly.js + animations)
└── README.md # 📄 You are here

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gemini-sql-assistant.git
cd gemini-sql-assistant

### 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Set up your .env file
Create a .env file in the root directory:

    GEMINI_API_KEY=your_google_gemini_api_key
    DB_HOST=localhost
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_PORT=5432

##🚀 Running the App
uvicorn main:app --reload

Visit: http://localhost:8000
The FastAPI Swagger UI is also available at:
http://localhost:8000/docs

## 🌐 Web Interface (Frontend)
- Accepts natural language questions (e.g., "Show RoAS per item.")

- Displays:

-- The generated SQL query (with typing animation)

-- Tabular query results

-- Interactive visualizations:

--- 📊 Bar Charts for per-item metrics

--- 📈 Line/Scatter Charts for time trends

📊 Visualization Logic
Charting is conditional:

- ✅ Displayed only for suitable data (e.g., item_id, date groupings)

- ❌ Skipped for single aggregated metrics

Handled via Plotly.js.

## 🧪 Example Prompts
| Prompt                       | Output                       |
| ---------------------------- | ---------------------------- |
| Show RoAS per item           | SQL + RoAS table + bar chart |
| Trend of ad spend over time  | SQL + trendline              |
| Total units sold last 7 days | SQL + table only             |

## 🧠 Tech Stack
- 🔮 Gemini 2.5 Pro (Google Generative AI)

- 🐍 FastAPI (Python backend)

- 🐘 PostgreSQL (RDBMS)

- 🎨 Plotly.js (Visualization)

- 🌐 HTML/CSS/JavaScript (Frontend)


👨‍💻 Author
T. Pothan Sai
PothanSai2004 • www.linkedin.com/in/pothansai0408 • pothansaithummala@gmail.com
