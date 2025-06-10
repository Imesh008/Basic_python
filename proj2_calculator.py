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

    def subtract(self,a,b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a,b):
        result = a * b
        self.history.append (f"{a} * {b} = {result}")
        return result
    
    def divide(self, a,b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power (self , a, b):
        result = a ** b
        self.history.append(f"{a} ** {b} = {result}")
        return result

    def modulus (self, a, b):
        result = a % b
        self.history.append(f"{a} % {b} = {result}")
        return result

    def show_history(self):
        if not self.history:
            return ("No history available.")
        else:
            print(" History:")
            for idx, item in enumerate(self.history, start=1):
                print(f"{idx}. {item}")

    def clear_history(self):
        self.history.clear()
        return ("History cleared...")
    

class CalculatorApp:
    def __init__ (self):
        self.calculator = Calculator()  #create an instance of the Calculator class
        
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

        def run(self):
            while True:
                self.show_menu()
                choice = input("Choose an option (1-9): ")

                #Improve input validation
                if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    print("Invalid option. Please try again.")
                    continue

                if choice == "9":
                    print("Thank you for using the calculator ...!")
                    print("Have a great day...!")
                    break


                elif choice == "8":
                    self.calculator.clear_history()
                    input("Press Enter to continue...")
                    print("History cleared...")
                    continue


                elif choice == "7":
                    self.calculator.show_history()
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
            
        

                    #Perform the operation based on user choice
                    try:
                        if choice == "1":
                            result = self.calculator.add(num1, num2)

                        elif choice == "2":
                            result = self.calculator.subtract(num1, num2)

                        elif choice == "3":
                            result = self.calculator.multiply(num1, num2)

                        elif choice == "4":
                            result = self.calculator.divide(num1, num2)

                    elif choice == "5":
                        result = self.calculator.power(num1, num2)

                    elif choice == "6":
                        result = self.calculator.modulus(num1, num2)

                     
                    print(f"Result: {result}")
                    input("Press Enter to continue...")
                    continue
                else:
                    print("Invalid option. Please try again.")
                    continue

                        

#run the calculator app
if __name__ == "__main__":
    app = CalculatorApp()
    app.run()  # Start the calculator application