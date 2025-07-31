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
    with open(FILE_NAME, 'r') as f:
        lines = f.readlines()

    if not lines:
        print ("No expenses to delete.\n")
        return
    
    print (f"\n📂 Select an expense to delete: ")
    for idx, line in enumerate(lines):
        date, amount, category, description = line.strip().split(',', 3)
        print(f"{idc + 1}. {date} - {amount} - {category} - {description}")

        try:
            choice = int(input("Enter the number of the entry to delete : ")) -1
            if  choice < 0 or choice >= len(lines):
            if confirm = input ("Are you sure you want to dele this entry? (y/n): ").lowee()
            if confirm == 'y':
                del lines[choice]
                with open(FILE_NAME, 'w') as f:
                    f.writelines(lines)
                print("✅ Expense deleted successfully!\n")
            else:
                print("❌ Deletion cancelled.\n")    
        else:
            print("❌ Invalid choice. Please enter a valid number.\n")
        except ValueError:

 
#add new options in the menue
def main_menu():
    while True:
        print("====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Summary")
        print("4. Filter Expenses by Category")
        print("5. Filter Expenses by date")
        print("6. Delete an Expense")
        print("7. Exit")
        choice = input("Choose an option (1-7): ").strip()

        if choice == '1':
            add_expense()

        elif choice == '2':
            view_expenses
        
        elif choice == '3':
            show_summary()

        elif choice == '4':
            filter_expenses_by_category()

        elif choice == '5':
            filter_expenses_by_date()

        elif choice == '6':
            delete_expense()

        elif choice == '7':
            print("Exiting the Expense Tracker. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please select a valid option (1-7).\n")



#export filtered data to another file
def export_filtered_data():
    category = input("Enter category to export: ").strip().lower()
    export_file = f"filtered_expenses_{category}.txt"
