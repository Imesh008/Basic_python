#a simple calculator in python

class Calculator:
    def __init__(self):
        self.history = []
        self.welcome_message = "Welcome to the Python Calculator"   #add a welcome message
        print(self.welcome_message)  # Display the welcome message
        print("_" * 25)  # Print a line for better readability
  
    def add(self, a,b): 
        result = a + b
        self.history.append(f"{a} + {b} = {result}")  #store the result in history
        return result 

    def substract(self,a,b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a,b):
        return a * b
    
    def divide(self, a,b):
        return a / b if b != 0 else "Cannot divide by zero"  #check for division by zero
    
    def power (self , a, b):
        return a ** b

    def modulus (self, a, b):
        return a % b
    


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
    print("8. Clear History")
    print("9. Exit")
    print("_" * 25)

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

#defines power function
def power (a, b):
    return a ** b

#Defines modulus function
def modulus (a,b):
    return a % b

#store history of calculations
history = []

print ("_" * 25)


#Input loop to choose and show option
while True :
    show_menu ()
    choice = input ("Choose an option (1-9): ")

    #Improve input validation
    if choice not in ["1", "2" ,"3" ,"4" ,"5" ,"6", "7" , "8" , "9"]:
       print("Invalid option. Please try again.")
       continue
  

    if choice == "9": #Choice number 9
        print ("Thank you for using the calculator ...!")
        print ("Have a great day...!")        #exit message
        break

    elif choice == "8":
        history.clear()
        print("History cleared...")
    
    elif choice == "7":
        #Show history of calculations
        print("History: ")
        if not history:             #check if history is empty
            print("No history available.")
        else:
            #Enumerate history with index
            for idx, item in enumerate(history, start=1):
                print(f"{idx}. {item}")
        input("Press Enter to continue...")
        continue
 
#Input numbers
#Add try-except for number input
    elif choice in ["1", "2", "3", "4", "5", "6"]:
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
        history.append(f"{num1} - {num2} = {result}")
        print ("Result: ", result)
        input ("Press Enter to continue...")


    elif choice == "3":
        result = multiply (num1, num2)
        history.append(f"{num1} * {num2} = {result}")
        print ("Result: ", result)
        input ("Press Enter to continue...")


    elif choice == "4":
        result =divide (num1, num2)
        history.append (f"{num1} / {num2} = {result}")
        print ("Result: ", result)
        input ("Press Enter to continue...")

        
    elif choice == "5":
        result = power (num1, num2)
        history.append(f"{num1} ** {num2} = {result}")
        print ("Result: ", result)
        input ("Press Enter to continue...")


    elif choice == "6":
        result = modulus (num1, num2)
        history.append(f"{num1} % {num2} = {result}")
        print("Result: ", result)
        input("Press Enter to continue...")
 
    else:
        print("Invalid option... Try again...")
    print ("_" * 25)  #print line for better readability
     