# finops-analyzer.py
# Basic analyzer for cloud billing CSV using AI-based logic

import sys
import pandas as pd

def analyze_spend(file_path):
    try:
        df = pd.read_csv(file_path)
        df['Cost'] = df['Cost'].astype(float)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Month'] = df['Date'].dt.to_period("M")

        total_cost = df['Cost'].sum()
        print(f"Total Cloud Spend: ${total_cost:.2f}")

        monthly = df.groupby('Month')['Cost'].sum()
        print("\nMonthly Breakdown:")
        print(monthly)

        top_services = df.groupby('Service')['Cost'].sum().sort_values(ascending=False).head(5)
        print("\nTop 5 Cost Drivers:")
        print(top_services)

        forecast = monthly.mean() * 12
        print(f"\nEstimated Annual Spend (based on average): ${forecast:.2f}")

    except Exception as e:
        print(f"Failed to analyze cost: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python finops-analyzer.py <billing-csv-file>")
        sys.exit(1)
    analyze_spend(sys.argv[1])