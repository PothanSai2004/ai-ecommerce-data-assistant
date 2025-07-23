import google.generativeai as genai

# Paste your API key here
genai.configure(api_key="AIzaSyBUDPRLWgL_9ydr6ADHofswBn_QBvzi7nw")

model = genai.GenerativeModel('gemini-2.5-pro')

response = model.generate_content("Write a SQL query to get total sales from a table called sales_data")
print(response.text)
