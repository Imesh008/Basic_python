#get user input
name= input("Enter your name: ")  #get user input
age= int(input("Enter your age: "))
print(f"Hello,{name}!, You are {age} , years old.")
print("-" * 20)

#example using variables
current_year = 2025
birth_year =current_year- age #estimate birth year
print(f"You were probably born in { birth_year}")
