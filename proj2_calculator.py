#a simple calculator in python

#display the menu
def show_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Substract")
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
#input loop to show choose option
while True :
    show_menu ()
    choice = input ("Choose an option (1-5): ")

    if choice == "5":   #choice number 5 
        print ("Existing calculator... Goodbye ...!")
        break


#input numbers
num1 = float(input("Enter fisrt number: "))
num2 = float(input("Enter second number: "))
#getting user inputes
 