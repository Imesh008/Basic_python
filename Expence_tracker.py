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
            f.write(f"{date},{amount},{category},{description}\n")
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
        print (f"{'Date':<12} {'Amount(RS)':<10} {'Category':<15} {'Description'}")
        print("-" * 50)
        for line in lines:
            date, amount, category, description = line.strip().split(',', 3)
            print(f"{date:<12} {amount:<10} {category:<15} {description}")
    print()


#show summary
def show_summary():     
    total = 0.0
    print("\n📈 Expense Summary:")
    with open(FILE_NAME, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len (parts) >=2:
                total += float(parts[1])
    print(f"\n💰 Total Expenses: Rs. {total:.2f}\n")

#filtered by category
def filter_expenses_by_category():
    keyword = input ("Enter category to filter: ").strip().lower()
    print (f"\n Filterd by Category: {keyword}")
    with open (FILE_NAME, 'r') as f:
        found = False
        for line in f:
            date, amount, category, description = line.strip().split(',',3)
            if category.lower() == keyword:
                print(f"{date:<12} {amount:<10} {category:<15} {description}")
                found = True
        if not found:  
            print("No expenses found for this category.\n")  


#delete an expense by index           #######################################################from theere
def delete_expense():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print ("No expenses recorded yet.\n")
        return

    with open(FILE_NAME, 'r') as f:
        expenses = f.readlines()

    if not expenses: #extra safety 
        print ("No expenses to delete.")
        return

    for idx, line in enumerate(expenses, start=1):
        print (f"{idx}. {line.strip()}")

    try:
        choice = int(input("Enter the number of the expense to delete: "))
        if 1 <= choice <= len(expenses):
            deleted = expenses.pop(choice - 1)
            print(f"✅ Deleted expense: {deleted.strip()}\n")

            #save back to the file
            with open(FILE_NAME, 'w') as f:
                f.writelines(expenses)
    
        else:
            print("❌ Invalid choice. No expense deleted.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")


#export filtered data 
def export_filtered_data():
    category = input ("Enter category to export: ").strip().lower()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")    #unique time suffix
    export_file = f"filtered_expenses_{category}_{timestamp}.txt"

    count = 0
    with open(FILE_NAME, 'r') as f, open (export_file, 'w') as f_out:
        for line in f:
            date, amount, cat, description = line.strip().split(',', 3)
            for line in f:
                date, amount, cat, description = line.strip().split(',', 3)
                if cat.lower() == category:
                    f_out.write(line)
                    count += 1

    if count > 0:

#export filtered data to another file
def filter_expenses_by_date():
    date_filter = input("Enter date to filter (YYYY-MM-DD): ").strip()
    print (f"\n📅 Expenses on {date_filter}:")
    found = False
    with open (FILE_NAME, 'r') as f:
        for line in f:
            date, amount, category, description = line.strip().split(',', 3)
            if date == date_filter:
                print(f"{date:<12} {amount:<10} {category:<15} {description}")
                found = True
    if not found:
        print("No expenses found for this date.\n")


#view and sort expenses
def view_sorted_expenses():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("No expenses recorded yet.\n")
        return
    with open(FILE_NAME, 'r') as f:
        lines = f.readlines()

    sorted_expenses = sorted(lines, key=lambda x: datetime.strptime(x.split(',')[0], "%Y-%m-%d"))
    print(f"\n📊 Sorted Expenses:") 
    for line in sorted_expenses:
        date, amount, category, description = line.strip().split(',', 3)
        print(f"{date:<12} {amount:<10} {category:<15} {description}")

#add these to the menu
def main_menu():
    while True:
        print("====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Summary")
        print("4. Filter Expenses by Category")
        print("5. Filter Expenses by Date")
        print("6. Delete an Expense")
        print("7. Export Filtered Data")
        print("8. View Sorted Expenses")
        print("9. Exit")
        choice = input("Choose an option (1-9): ").strip()

        if choice == '1':
            add_expense()

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            show_summary()

        elif choice == '4':
            filter_expenses_by_category()

        elif choice == '5':
            filter_expenses_by_date()

        elif choice == '6':
            delete_expense()

        elif choice == '7':
            export_filtered_data()

        elif choice == '8':
            view_sorted_expenses()

        elif choice == '9':
            print("Exiting the Expense Tracker. Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice. Please select a valid option (1-9).\n")
    
if __name__ == "__main__":
    main_menu()
     