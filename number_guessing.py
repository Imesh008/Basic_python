import random 

print("-"*30)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("-"*30)

def play_game():
    number_to_guess = random.randint(1, 100) 
    attempts = 0 
    difficulty = input("Choose difficulty (Easy/Medium/Hard): ").lower()
    max_attempts = 10 if difficulty == "easy" else 7 if difficulty == "medium" else 5
    guess = int(input("Guess a number between 1 and 100: "))


    while guess != number_to_guess:
        attempts += 1
        if guess < number_to_guess:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
        if attempts >= max_attempts:
            break
        guess = int(input("Try again: "))


    if guess == number_to_guess:
        print(f"🎉 You guessed it in {attempts} attempts!")
    else:
        print (f"😞 You've used all your attempts. The number was {number_to_guess}.")
    with open ("scores.txt", "a") as file:
        file.write(f"{difficulty} - {attempts} attempts\n")
    print("-"*30)

try:
    print(open("scores.txt").read())
except FileNotFoundError:
    print("No scores recorded yet.")


while True:
    play_game()
    again = input ("Do you want to play again? (yes/no): ").lower
    if again != 'y':
        break

print("👋 Thanks for playing!")


 
 
 
 
 
   = 10     == "easy" else 7 if difficulty == "medium" else 5
#Ask user for the first guess

guess = int(input("Guess a number between 1 and 100: "))

while guess != number_to_guess:
    attempts += 1        #Counting attempts

    if guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    #Stop if attempts are finished
    if attempts >= max_attempts:
        break

    guess = int(input("Try again: "))

# Final result message
if guess == number_to_guess:
    attempts += 1         # Counting the last attempt
    print(f"🎉 You guessed it in {attempts} attempts!")
else:
    print(f"😞 You've used all your attempts. The number was {number_to_guess}.")

    
print("-"*30)