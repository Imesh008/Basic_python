#simple to-do list
tasks = []   #initialize the tasks list

#define a function
def add_tasl(task):
    tasks.append(task)

#define show_tasks function
def show_tasks():
    for i , task in enumerate (tasks , 1) :
        print (f"(i). {task}")