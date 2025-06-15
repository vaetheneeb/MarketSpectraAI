from openai import OpenAI
import os

# Initialize OpenAI client (you'll need to set OPENAI_API_KEY in your environment)
client = OpenAI()

def get_ai_response(question, report_data):
    """
    Get AI response to user question based on the report data.
    In a real implementation, you would structure the report data into a suitable prompt.
    """
    try:
        # Create a text summary of the report data for the prompt
        report_summary = f"""
        Company: {report_data['company_name']}
        Quarter: Q{report_data['quarter']} {report_data['year']}
        
        Income Statement Highlights:
        - Revenue: {report_data['income_statement'][0]['Revenue']}
        - Net Profit: {report_data['income_statement'][0]['Net Profit']}
        - EPS: {report_data['income_statement'][0]['EPS']}
        
        Balance Sheet Highlights:
        - Total Assets: {report_data['balance_sheet'][0]['Total Assets']}
        - Total Liabilities: {report_data['balance_sheet'][0]['Total Liabilities']}
        - Debt-to-Equity: {report_data['balance_sheet'][0]['Debt-to-Equity']}
        
        Question: {question}
        """
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a financial analyst assistant. Provide concise, accurate answers based on the quarterly report data."},
                {"role": "user", "content": report_summary}
            ],
            temperature=0.3
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Sorry, I couldn't process your request. Error: {str(e)}" 