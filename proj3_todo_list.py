import os

#File where tasks are stored
TASK_FILE = 'tasks.txt'

#convert this in to OOP
class Todolist:
    def __init__(self):
        self.tasks = self.load_tasks()
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
        for task in tasks:
            file.write(task + '\n')
    print(f"Saved {len(tasks)} tasks to {TASK_FILE}")       #Confirm taks saved



#Display menu options to the users 
def display_menu():
    print ("\n" + "="*30)
    print ("---- TODO LIST MENU ----")
    print ( "="*30)
    print ("1. Add tasks")
    print ("2. View tasks")
    print ("3. Remove tasks")
    print ("4. Save tasks")
    print ("5. Delete all tasks")
    print ("6. Exit program")
    print ("="*30 + "\n")


#View tasks in the list
def view_tasks(tasks):
    print("\n" + "="*30)
    print("YOUR TASKS: ")
    print("="*30)
    if not tasks:
        print("No tasks available...")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print("="*30 + "\n")        


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
        choice = input ("Enter your choice (1-6): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice =="3":
            remove_task(tasks)

        elif choice == "4":
            save_tasks(tasks)

        elif choice == "5":
            clear_confirm = input("Are you sure you want to delete all tasks? (yes/no): ").strip().lower()
            if clear_confirm == "yes" or clear_confirm == "y":
                tasks.clear()
                print("All tasks have been deleted successfully...!")
            else:
                print("No tasks were deleted...")
                
        elif choice == "6":
            confirm = input("Do you want to  save tasks before exiting? (yes/no): ").strip().lower()
            if confirm == "yes" or confirm == "y":
                save_tasks(tasks)
            print("Exiting the program. Goodbye!...")
            break
        else:
            print("Invalid choice. Please try again...")


if __name__ == "__main__":
    main()        


 