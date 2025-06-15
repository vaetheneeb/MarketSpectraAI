class FinancialDataExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.financial_data = {}  # Initialize the attribute

    def extract(self):
        # Example extraction logic (replace with your actual logic)
        # After extracting, always set self.financial_data
        self.financial_data = {
            "revenue": 100,
            "gross_profit": 60,
            "net_profit": 30,
            # Add other fields as needed
        }
        return self.financial_data 