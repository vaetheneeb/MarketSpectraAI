import pandas as pd

def get_sample_data():
    """
    Provides sample financial trend data for demonstration purposes.
    In a real application, this would typically fetch historical data from a database or API.

    Returns:
        pd.DataFrame: A DataFrame with sample financial data over quarters.
    """
    data = {
        "Quarter": ["Q1 2023", "Q2 2023", "Q3 2023", "Q4 2023", "Q1 2024", "Q2 2024"],
        "Revenue": [100000, 110000, 125000, 130000, 135000, 140000],
        "Net Profit": [15000, 17000, 19000, 21000, 22000, 23000]
    }
    return pd.DataFrame(data)