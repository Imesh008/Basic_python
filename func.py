#creat a funtion
def greet (name):
    return "Hello ," + name + "!"  #recall func

#print func
print(greet("Ayesh"))

print("-"*25)

#create a list
fruits=["apple","banana","cherry"]  #list

#append item to the list
fruits.append ("mango")

#for loop to print each fruit
for fruit in fruits:
    print(fruit)

#wrap print loop in to the function
def print_fruits (fruit_list):
    for fruit in fruit_list:
        print(fruit)
print_fuits(fruits)