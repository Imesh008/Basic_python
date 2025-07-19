import os
from datetime import datetime

#create a file to store expenses
FILE_NAME = 'expenses.txt'


#create a file if it don't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w') as f:
        pass


#function to add an expense
def add_expense():
    try:
        amount = float(input("Enter amount(RS): "))
        category = input("Enter category(Food, Travel, etc.): ").strip()
        description = input("Enter description: ").strip()
        date = input("Enter date (YYYY-MM-DD) or leave a blank for today: ").strip()
        
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
       
        with open (FILE_NAME, 'a') as f:
            f.write(f"{date}, {amount}, {category}, {description}\n")
        print("✅ Expense added successfully!\n")
    except ValueError:
        print("❌ Invalid input. Please enter a numeric amount.\n")

#function to view all expenses
def view_expenses():
    total_expenses = 0
    with open(FILE_NAME, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len (parts) >=2:
                total += float(parts[1])
    print(f"\n💰 Total Expenses: Rs. {total:.2f}\n")

    #Main menu loop
