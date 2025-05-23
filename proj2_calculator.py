#a simple calculator in python

#add a welcome message
print("Welcome to the Python Calculator")

#display the menu
def show_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Show History")
    print("8. Exit")

#addition function
def add (a, b):
    return a + b

#subtraction function
def subtract (a, b):
    return a - b

#define multiply function
def multiply(a, b):
    return a * b

#define divide function with zero check
def divide (a, b):
    if b== 0:
        return "Cannot divide by zero"
    return a / b

#defines power funtion
def power (a, b):
    return a ** b

#defines modulus function
def modulus (a,b):
    return a % b

#store history of calculations
history = []

print ("_" * 25)


#input loop to show choose option
while True :
    show_menu ()
    choice = input ("Choose an option (1-8): ")

    #improve input validation
    if choice not in ["1", "2" ,"3" ,"4" ,"5" ,"6", "7" , "8"]:
       print("Invalid option. Please try again.")
       continue
  

    if choice == "8":   #choice number 8
        print ("Exiting calculator... Goodbye ...!")
        print("Thanks for using the calculator...!")        #exit message
        break

    
    elif choice == "7":
        print("History: ")
        if not history:
            print("No history available.")
        else:
            for item in history:
                print(item)
        input ("Press Enter to continue...")
        continue

#Input numbers
#add try-except for number input
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: ")) #getting user inputs
    except ValueError:
        print("Invalid input. Please enter numbers only...!")
        continue
     
 

    if choice == "1":
        result= add(num1 ,num2)
        history.append(f"{num1} + {num2} = {result}")
        print("Result: ", result)
        input ("Press Enter to continue...")


    elif choice == "2":
        result = subtract(num1, num2)
        history.appen(f"{num1}-{num2} = {result}")
        print ("Result: ", result)
        input ("Press Enter to continue...")


    elif choice == "3":
        result = multiply (num1, num2)
        history.append()

    elif choice == "4":
        print ("Result: ",divide(num1, num2))
        input ("Press Enter to continue")

    elif choice == "5":
        print ("Result: ", power(num1, num2))
        input ("Press Enter to continue")

    elif choice == "6":
        print ("Result: ", modulus(num1, num2))
        input ("Press Enter to continue")

 
    else:
        print("Invalid option... Try again...")


 