#creat a basic dictionary
person ={"name":"Ravi","age":30}

#access a value using a key
print(person["name"])

#add a new key value pair to the dictionary
person["city"]="colombo"

#loop throught the keys and values in the dictionary
for key,value in person.items():
    print(key, ":", value)


print("-"*25)

#creat a basic tuple
colors =("red","green","blue")

#access item in the tupple
print(colors[1])   

#loop through the tuple
for color in colors:
    print(color)

#combine dictionary and tuple useage
favourite = {"Ravi":colors[0]}   #ravi likes red
print(favourite)