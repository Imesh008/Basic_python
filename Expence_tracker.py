import os
from datetime import datetime

#create a file to store expenses
FILE_NAME = 'expenses.txt'


#create a file if it don't exist
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, 'w').close()


#function to add an expense
def add_expense():
    

               

        