import os

#file where tasks will be stored
TASK_FILE = 'tasks.txt'


#loads tasks from the file into a list
def lead_tasks():
    #creat a file if it does not exist
    if not os.path.ecists(TASK_FILE):
        open(TASK_FILE, 'w').close()
    
    #read each line and return a list of tasks
    with open (TASK_FILE, 'r') as file:
        return [line.strip() for line in file.read()]
    


#saves tasks to the file
def save_tasks(tasks):
    with open (TASK_FILE, "w") as file:
        for task in taks:
            file.write(task + '\n')
    print(f"Saved {len(tasks)} tasks to {TASK_FILE}")       #arrange print to confirm that tasks saved nicely



#display menue options to the users 

def display_menu():
    print ("\nTodo List Menu:")
    print ("1. View tasks")
    print ("2. Add tasks")
