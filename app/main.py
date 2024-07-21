# main.py
from fastapi import FastAPI, File, UploadFile
import pandas as pd
import openai
from io import BytesIO

app = FastAPI()

# Initialize OpenAI API Key
openai.api_key = "sk-None-Clo1HR5P1Bev9ItC2vooT3BlbkFJOwWf6W4jxHulezewa5Pn"

@app.post("/analyze-sales-data/")
async def analyze_sales_data(file: UploadFile = File(...)):
    # Read the uploaded file into a pandas DataFrame
    content = await file.read()
    if file.filename.endswith('.csv'):
        df = pd.read_csv(BytesIO(content))
    elif file.filename.endswith('.json'):
        df = pd.read_json(BytesIO(content))
    elif file.filename.endswith('.xlsx'):
        df = pd.read_excel(BytesIO(content))
    else:
        return {"error": "Unsupported file type"}

    # Convert DataFrame to JSON for LLM input
    data_json = df.to_json(orient='records')

    # Prepare the prompt for the LLM
    prompt = f"""
    Analyze the following sales data and provide insightful feedback on the performance of individual sales representatives and the overall sales team. Also, assess sales performance trends and make forecasts based on the data:

    Sales Data: {data_json}
    """

    # Call the LLM using the latest OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-instruct",  # Use the appropriate LLM model
        messages=[
            {"role": "system", "content": "You are a data analyst."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )

    analysis = response.choices[0].message['content'].strip()

    return {"analysis": analysis}
