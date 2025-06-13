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
    