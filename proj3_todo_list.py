import os

#File where tasks are stored
TASK_FILE = 'tasks.txt'

#convert this in to OOP
class Todolist:
    def __init__(self):
        self.tasks = self.load_tasks()

    #Loads tasks from the file into a list
    def load_tasks(self):
        #Create a file if it does not exist
        if not os.path.exists(TASK_FILE):
            open(TASK_FILE, 'w').close()
    
        #Read each line and return a list of tasks
        with open (TASK_FILE, 'r') as file:
            return [line.strip() for line in file.readlines()]
    


#Saves tasks to the file
    def save_tasks(self):
        with open (TASK_FILE, "w") as file:
            for task in self.tasks:
                file.write(task + '\n')
        print(f"Saved {len(self.tasks)} tasks to {TASK_FILE}")       #Confirm taks saved



#Display menu options to the users 
    def display_menu(self):
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
    def view_tasks(self):
        print("\n" + "="*30)
        print("YOUR TASKS: ")
        print("="*30)
        if not self.tasks:
            print("No tasks available...")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        print("="*30 + "\n")        


    #Add a task to the list
    def add_task(self):
        task = input("Enter the task to add: ")
        self.tasks.append(task)
        print("Task added successfully...! \n")

    #Remove task from the list 
    def remove_task (self):
        self.view_tasks()
        try:
            index = int(input("Enter the task number to remove: ")) - 1
            if 0<= index < len(self.tasks):
                removed = self.tasks.pop(index)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number...")

        except ValueError:
            print("Please enter a number...")

    #Delete all tasks from the list
    def delete_all_tasks(self):
        confirm = input("Are you sure you want to delete all tasks? (yes/no): ").strip().lower()
        if confirm == "yes" or confirm == "y":
            self.tasks.clear()
            print("All tasks have been deleted successfully...!")



        #Main app loop creation
        def run(self):
                while True:
                    self.display_menu()
                    choice = input("Enter your choice (1-6): ")

                    if choice == "1":
                        self.add_task()

                    elif choice == "2":
                        self.view_tasks()

                    elif choice == "3":
                        self.remove_task()

                    elif choice == "4":
                        self.save_tasks()

                elif choice == "5":
            clear_confirm = input("Are you sure you want to delete all tasks? (yes/no): ").strip().lower()
            if clear_confirm == "yes" or clear_confirm == "y":
                self.tasks.clear()
                print("All tasks have been deleted successfully...!")
            else:
                print("No tasks were deleted...")

        elif choice == "6":
            confirm = input("Do you want to save tasks before exiting? (yes/no): ").strip().lower()
            if confirm == "yes" or confirm == "y":
                self.save_tasks()
            print("Exiting the program. Goodbye!...")
            break
        else:
            print("Invalid choice. Please try again...")

    
if __name__ == "__main__":
    app = Todolist()
    app.run()     


 