import os
from datetime import datetime
from collections import defaultdict

FILE_NAME = 'expenses.txt'

# Create the file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w') as f:
        pass


# Function to add an expense
def add_expense():
    try:
        amount = float(input("Enter amount (Rs): "))
        category = input("Enter category (Food, Travel, etc.): ").strip()
        description = input("Enter description: ").strip()
        date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()

        if not date_input:
            date_input = datetime.now().strftime("%Y-%m-%d")
        else:
            # Validate date format
            try:
                datetime.strptime(date_input, "%Y-%m-%d")
            except ValueError:
                print("❌ Invalid date format. Use YYYY-MM-DD")
                return

        with open(FILE_NAME, 'a') as f:
            f.write(f"{date_input},{amount},{category},{description}\n")
        print("✅ Expense added successfully!\n")
    except ValueError:
        print("❌ Invalid input. Please enter a numeric amount.\n")


# Function to view all expenses
def view_expenses():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("📊 No expenses recorded yet.\n")
        return

    print("\n📊 All Expenses:")
    with open(FILE_NAME, 'r') as f:
        lines = f.readlines()
        print(f"{'Date':<12} {'Amount(Rs)':<12} {'Category':<15} {'Description'}")
        print("-" * 60)
        for line in lines:
            date, amount, category, description = line.strip().split(',', 3)
            print(f"{date:<12} {amount:<12} {category:<15} {description}")
    print()


# Function to show summary
def show_summary():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("❌ No expenses recorded yet.\n")
        return

    total = 0.0
    category_totals = defaultdict(float)
    with open(FILE_NAME, 'r') as f:
        for line in f:
            date, amount, category, description = line.strip().split(',', 3)
            total += float(amount)
            category_totals[category] += float(amount)

    print(f"\n💰 Total Expenses: Rs {total:.2f}")
    print("📂 Breakdown by Category:")
    for cat, amt in category_totals.items():
        print(f"   - {cat}: Rs {amt:.2f}")
    print()


# Function to filter or export expenses by category or date
def filter_export(exp_type='category', export=False):
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("❌ No expenses recorded yet.\n")
        return

    if exp_type == 'category':
        filter_input = input("Enter category to filter: ").strip()
        print(f"\n📂 Filtered by Category: {filter_input}")
    else:
        filter_input = input("Enter date to filter (YYYY-MM-DD): ").strip()
        # Validate date
        try:
            datetime.strptime(filter_input, "%Y-%m-%d")
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD")
            return
        print(f"\n📅 Filtered by Date: {filter_input}")

    header = f"{'Date':<12} {'Amount(Rs)':<12} {'Category':<15} {'Description'}"
    print(header)
    print("-" * 60)

    count = 0
    export_file = ''
    if export:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        export_file = f"filtered_expenses_{filter_input}_{timestamp}.txt"

    with open(FILE_NAME, 'r') as f, open(export_file, 'w') if export else open(os.devnull, 'w') as f_out:
        for line in f:
            date, amount, category, description = line.strip().split(',', 3)
            match = False
            if exp_type == 'category' and category.lower() == filter_input.lower():
                match = True
            elif exp_type == 'date' and date == filter_input:
                match = True

            if match:
                print(f"{date:<12} {amount:<12} {category:<15} {description}")
                if export:
                    f_out.write(line)
                count += 1

    if count == 0:
        print("❌ No matching expenses found.\n")
    elif export:
        print(f"✅ Exported {count} expenses to {export_file}\n")
    else:
        print()


# Function to delete an expense
def delete_expense():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("❌ No expenses recorded yet.\n")
        return

    with open(FILE_NAME, 'r') as f:
        expenses = f.readlines()

    if not expenses:
        print("❌ No expenses to delete.\n")
        return

    for idx, line in enumerate(expenses, start=1):
        print(f"{idx}. {line.strip()}")

    try:
        choice = int(input("Enter the number of the expense to delete: "))
        if 1 <= choice <= len(expenses):
            deleted = expenses.pop(choice - 1)
            print(f"✅ Deleted expense: {deleted.strip()}\n")
            with open(FILE_NAME, 'w') as f:
                f.writelines(expenses)
        else:
            print("❌ Invalid choice. No expense deleted.\n")
    except ValueError:
        print("❌ Invalid input. Please enter a number.\n")


# Function to view sorted expenses by date
def view_sorted_expenses():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        print("❌ No expenses recorded yet.\n")
        return

    with open(FILE_NAME, 'r') as f:
        lines = f.readlines()

    try:
        sorted_expenses = sorted(lines, key=lambda x: datetime.strptime(x.split(',')[0], "%Y-%m-%d"))
    except ValueError:
        print("❌ Some dates in the file are invalid.\n")
        return

    print("\n📊 Sorted Expenses by Date:")
    print(f"{'Date':<12} {'Amount(Rs)':<12} {'Category':<15} {'Description'}")
    print("-" * 60)
    for line in sorted_expenses:
        date, amount, category, description = line.strip().split(',', 3)
        print(f"{date:<12} {amount:<12} {category:<15} {description}")
    print()


# Main menu
def main_menu():
    while True:
        print("====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Summary")
        print("4. Filter Expenses by Category")
        print("5. Filter Expenses by Date")
        print("6. Delete an Expense")
        print("7. Export Expenses by Category")
        print("8. Export Expenses by Date")
        print("9. View Sorted Expenses")
        print("10. Exit")

        choice = input("Choose an option (1-10): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_summary()
        elif choice == '4':
            filter_export('category')
        elif choice == '5':
            filter_export('date')
        elif choice == '6':
            delete_expense()
        elif choice == '7':
            filter_export('category', export=True)
        elif choice == '8':
            filter_export('date', export=True)
        elif choice == '9':
            view_sorted_expenses()
        elif choice == '10':
            print("Exiting the Expense Tracker. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please select a valid option (1-10).\n")


if __name__ == "__main__":
    main_menu()
