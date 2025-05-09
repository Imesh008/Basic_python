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

#wrap file rading in try/except
try:
    with open ("hello.txt" , "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found...! ")