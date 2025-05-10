#simple to-do list
tasks = []   #initialize the tasks list

#define a function
def add_task(task):
    tasks.append(task)

#define show_tasks function
def show_tasks():
    for i , task in enumerate (tasks , 1) :
        print (f"(i). {task}")

#add main loo structure
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice =input("choose: ")

#handle task addition option
if choice == "1":
    task = input ("Enter task: ")
    add_task(task)

#handle task addition option
elif choice == "2":
    show_tasks()
    
