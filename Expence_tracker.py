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
    print("\n📊 All Expenses:")
    if os.path.getsize(FILE_NAME) == 0:
        print("No expenses recorded yet.\n")
        return
    
    with open(FILE_NAME, 'r') as f:
        lines = f.readlines()
        print (f"{'Date':<12} {'Amount(RS)':<10} {'Category':<15} 'Description")
        print("-" * 50)
        for line in lines:
            date, amount, category, description = line.strip().split(',', 3)
            print(f"{date:<12} {amount:<10} {category:<15} {description}")
    print()

def show_summary():     
    total = 0.0
    print("\n📈 Expense Summary:")
    with open(FILE_NAME, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len (parts) >=2:
                total += float(parts[1])
    print(f"\n💰 Total Expenses: Rs. {total:.2f}\n")

#Main menu loop
def main_menu():
    while True:
        print("====== EXPENNSE TRACKER ======")
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. Show Total Summary")
            print("4. Exit")
            choice = input ("Choose and option (1-4): ").strip()

            if choice == '1':
                add_expense()

            elif choice == '2':
                view_expenses()

            elif choice == '3':
                show_summary()

            elif choice == '4':
                print("Exiting the Expense Tracker. Goodbye! 👋")
                break
            else:
                print("❌ Invalid choice. Please select a valid option (1-4).\n")


#start the porogram    
if name == "__main__":
    print("Welcome to the Expense Tracker! 📊")        
 


#filter expenses by category
def filter_expenses_by_category():
    keyword = input ("Enter category to filter: ").strip().lower()
    print (f"\n Filterd by Category: {keyword}")
    with open (FILE_NAME, 'r') as f:
        found = False
        for line in f:
            date, amount, category, description = line.strip().split(',',3)
            if date == keyword:
                print(f"{date:<12} {amount:<10} {category:<15} {description}")
                found = True
        if not found:  
            print("No expenses found for this category.\n")  


#delete an expense by index           
def delete_expense():
