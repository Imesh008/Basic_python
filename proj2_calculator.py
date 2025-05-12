#a simple calculator in python

#display the menu
def show_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Susbtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

#addition function
def add (a, b):
    return a + b

#substraction function
def substract (a, b):
    return a - b

#define multiply function
def multiply(a, b):
    return a * b

#define divide function with zero check
def divide (a, b):
     if b== 0:
        return "Cannot divide by zero"
    return a / b

print ("_" * 25)