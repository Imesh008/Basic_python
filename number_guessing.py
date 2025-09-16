import random 
number_to_guess =  random.randint (1, 100)

guess = int(input("Guess a number between 1 and 100: "))

while guess != number_to_guess:
    if guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    guess = int(input("Try again:"))

print("Congratulations! You've guessed the number:", number_to_guess)