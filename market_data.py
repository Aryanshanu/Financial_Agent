import pandas as pd

def get_financial_insights():
    # Replace with actual financial data fetching logic
    data = {
        "Stock": ["AAPL", "GOOGL", "AMZN"],
        "Price": [150.00, 2800.00, 3400.00],
        "Change": ["+1.5%", "-0.5%", "+2.0%"]
    }
    return pd.DataFrame(data)
