# Sales Team Performance Analysis with LLM

This project provides a FastAPI-based web service to analyze sales data using OpenAI's language models. The service accepts CSV, JSON, or Excel files, processes the data, and generates insightful feedback on the performance of individual sales representatives and the overall sales team. It also assesses sales performance trends and makes forecasts based on the provided data.

## Features

- Upload sales data in CSV, JSON, or Excel format.
- Analyze sales data using OpenAI's language models.
- Get detailed feedback on individual and team performance.
- Assess trends and make forecasts.

## Requirements

- Python 3.9 or later
- FastAPI
- Pandas
- OpenAI
- Uvicorn

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/sales-team-performance-analysis-llm.git
    cd sales-team-performance-analysis-llm
    ```

2. **Create a virtual environment:**(necessary)

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up OpenAI API key:**

    Replace `"sk-None-Clo1HR5P1Bev9ItC2vooT3BlbkFJOwWf6W4jxHulezewa5Pn"` with your actual OpenAI API key in `main.py`:

    ```python
    openai.api_key = "your-openai-api-key"
    ```

## Usage

1. **Start the FastAPI server:**

    ```sh
    uvicorn main:app --reload
    ```

2. **Access the API:**

    The API will be available at `http://127.0.0.1:8000`.

3. **Analyze Sales Data:**

    Send a POST request to `/analyze-sales-data/` with your sales data file.

    Example using `curl`:

    ```sh
    curl -X POST "http://127.0.0.1:8000/analyze-sales-data/" -F "file=@path/to/your/file.csv"
    ```

## Endpoint

- **POST `/analyze-sales-data/`**

    - **Description:** Analyze sales data and provide feedback.
    - **Parameters:**
        - `file`: The sales data file (CSV, JSON, or Excel format).
    - **Response:**
        - `analysis`: The analysis of the sales data.





1. **Receive the analysis:**

    ```json
    {
        "analysis": "Alice has a strong sales performance with consistent growth over the period. Bob's performance is stable but slightly lower than Alice's. The overall team shows a positive trend in sales."
    }
    ```
    

## Work Needed
- Testing  Endpoints properly
3.- Prompt Engineering 

- need more changes for the endpoints for the specifc usecases
-  and make a mircoservice architecture 
