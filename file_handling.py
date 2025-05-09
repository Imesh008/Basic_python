#create and opne a file for writing
with open("hello.txt" , "w") as file:
    file.write("Hello, file !")

#add print to confirm file write
print("File Written Successfully...")

#open and read the file content
with open("hello.txt" , "r") as file:
    content = file.read()
    print(content)
    print("Read the content")  #confirmation

#wrap file reading in try/except
try:
    with open ("hello.txt" , "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found...! ")

#test error handling with a missing file
try:
    with open ("hello.txt" , "r") as file:
        print (file.read())
except FileNotFoundError:
    print("Oops! File does not exist...")

#add general exception handler
except Exception as e:
    print("An error occurred:" , e)

#write and read multiple lines with a loop
with open ("data.txt" , "w") as file:
    file.write ("Line 1\nLine 2\nLine 3")

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())