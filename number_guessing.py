import random 
number_to_guess =  random.randint (1, 100)

guess = int(input("Guess a number between 1 and 100: "))

while guess != number_to_guess: