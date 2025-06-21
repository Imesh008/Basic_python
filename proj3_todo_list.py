import os

#File where tasks will be stored
TASK_FILE = 'tasks.txt'


#Loads tasks from the file into a list
def load_tasks():
    #Create a file if it does not exist
    if not os.path.exists(TASK_FILE):
        open(TASK_FILE, 'w').close()
    
    #Read each line and return a list of tasks
    with open (TASK_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]
    


#Saves tasks to the file
def save_tasks(tasks):
    with open (TASK_FILE, "w") as file:
        for task in (tasks):
            file.write(task + '\n')
    print(f"Saved {len(tasks)} tasks to {TASK_FILE}")       #Arrange print to confirm that tasks saved nicely



#Display menu options to the users 
def display_menu():
    print ("\n" + "="*30)
    print ("TODO LIST MENU")
    print ("\nTodo List Menu:")
    print ("1. View tasks")
    print ("2. Add tasks")
    print ("3. Remove tasks")
    print ("4. Save tasks")
    print ("5. Exit program")
    print ("="*30 + "\n")


#View tasks in the list
def view_tasks(tasks):
    print("\n" + "="*30)
    if not tasks:
        print("="*30)
    if not tasks: 
        print("No tasks available...")
    else:
        for i, task in enumerate (tasks, start=1):
            print(f"{i}. {task}")
            


#Add a task to the list
def add_task(tasks):
    task = input("Enter the task to add: ")
    tasks.append(task)
    print("Task added successfully...! \n")

#Remove task from the list 
def remove_task (tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0<= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number...")

    except ValueError:
        print("Please enter a number...")


#Main app loop creation
def main ():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input ("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice =="3":
            remove_task(tasks)

        elif choice == "4":
            save_tasks(tasks)

        elif choice == "5":
            confirm = input("Do you want to  save tasks before exiting? (yes/no): ").strip().lower()
            if confirm == "yes"or confirm == "y":
                save_tasks(tasks)
            print("Exiting the program. Goodbye!...")
            break
        else:
            print("Invalid choice. Please try again...")


if __name__ == "__main__":
    main()        


 