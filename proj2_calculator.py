#a simple calculator in python

#add a welcome message
print("Welcom to the Python Calculator")

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

    #improve input validation
    if choice not in ["1", "2" ,"3" "4" ,"5"]:
       print("Invalid option. Please try again.")
       continue
  

    if choice == "5":   #choice number 5 
        print ("Existing calculator... Goodbye ...!")
        break


#input numbers
#add try except for number input
try:
    num1 = float(input("Enter fisrt number: "))
    num2 = float(input("Enter second number: ")) #getting user inputes
except ValueError:
    print("Invalid input. Please enter numbers only...!")
     
 

if choice == "1":
    print ("Result: ", add(num1 ,num2))

elif choice == "2":
    print("Result: ", substract(num1, num2))

elif choice == "3":
    print ("Result: ", multiply (num1, num2))

elif choice == "4":
    print ("Result: ",divide(num1, num2))

else:
    print("Invalid option... Try again...")


 