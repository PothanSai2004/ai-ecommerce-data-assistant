import os
import re
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def generate_sql_from_question(question: str) -> str:
    prompt = f"""
You are a senior data analyst. Your job is to convert business questions into accurate SQL queries for PostgreSQL.

Only use the following **available tables and columns**:

### Tables:
1. total_sales_metrics (alias: t)
   - date
   - item_id
   - total_sales
   - total_units_ordered

2. ad_sales_metrics (alias: a)
   - date
   - item_id
   - ad_sales
   - impressions
   - ad_spend
   - clicks
   - units_sold

3. eligibility (alias: e)
   - eligibility_datetime_utc
   - item_id
   - eligibility
   - message

### SQL Response Rules:
- Output only **valid SQL code**. No explanations. No markdown. No ```sql.
- Always use table aliases (t, a, e) when referring to columns.
- Always fully qualify ambiguous columns with the correct alias (e.g., t.item_id).
- Join tables using both `item_id` and `date` unless told otherwise.
- Do not use columns that are not in the schema above.
- Date Filtering Rules:
  If user asks for "last N days", "past week", etc., use:
  `t.date >= CURRENT_DATE - INTERVAL 'N days'`
- For eligibility, the column `eligibility` contains TRUE or FALSE representing eligibility.
- If metric calculation may return NULL (e.g., division by zero), filter results using HAVING (e.g., `HAVING SUM(clicks) > 0`) to exclude nulls.

### For RoAS-related queries:
- RoAS (Return on Ad Spend) = SUM(t.total_sales) / NULLIF(SUM(a.ad_spend), 0)
- Assume the user wants **RoAS per item_id** unless the question says "overall".
- Return `item_id` and the computed RoAS value in the result.
- Group by `t.item_id` for full breakdown.

### Visualization-Specific Rules:
- Only generate SQL suitable for visualization **if** the user question implies comparison, breakdown, trend, ranking, grouping, or metrics per item or over time.
- Examples of visual-suitable questions:
  - "Show RoAS per item"
  - "Trend of sales over time"
  - "Top 10 products by ad spend"
- Do **not** return single aggregate values (e.g., total RoAS) for visualization.
- When visualization is relevant, return data structured to work with **Matplotlib** or **Plotly** (i.e., grouped results with `item_id`, `date`, or metrics).

### General Guidelines:
- Return all relevant item-level metrics unless explicitly asked for a single value.
- Make the output usable for **visualizations**, e.g., bar charts or trend lines.
- If asked for trends or time series, include `date` in the SELECT and GROUP BY.
- Always use NULLIF for denominators to avoid division by zero errors.
- Cost Per Click Rule: Always filter out items where SUM(clicks) = 0 using a HAVING clause when calculating CPC to avoid NULL results.

Now convert the following user question into a correct SQL query:

User question: "{question}"
"""
    response = model.generate_content(prompt)
    sql_raw = response.text.strip()

    cleaned_sql = re.sub(r"```sql\s*([\s\S]+?)```", r"\1", sql_raw, flags=re.IGNORECASE)
    cleaned_sql = re.sub(r"```([\s\S]+?)```", r"\1", cleaned_sql, flags=re.IGNORECASE)

    return cleaned_sql.strip()
