import pandas as pd
from datetime import datetime
import os

FILE = "expenses.csv"

# Create CSV if not exists
if not os.path.exists(FILE):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE, index=False)

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Shopping, etc): ")
    amount = float(input("Enter amount: "))
    
    df = pd.read_csv(FILE)
    df.loc[len(df)] = [date, category, amount]
    df.to_csv(FILE, index=False)
    
    print("✅ Expense added successfully!")

def view_summary():
    df = pd.read_csv(FILE)
    
    if df.empty:
        print("No expenses recorded yet.")
        return
    
    print("\n💰 Total Spending:", df["Amount"].sum())
    print("\n📊 Category-wise Spending:")
    print(df.groupby("Category")["Amount"].sum())

while True:
    print("\n--- Smart Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_summary()
    elif choice == "3":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice!")
