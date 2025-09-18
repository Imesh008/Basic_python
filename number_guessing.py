import random 

number_to_guess =  random.randint (1, 100)
attempts = 0
difficulty = input ("Choose difficulty (Easy/Medium/Hard): ").lower()
max_attempts = 10 if difficulty == "easy" else 7 if difficulty == "medium" else 5
 

guess = int(input("Guess a number between 1 and 100: "))

while guess != number_to_guess:
    attemps += 1
    if guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    if attemps >= max_attempts:
        break
    guess = int(input("Try again:"))


if guess == number_to_guess:
    print(f"🎉 You guessed it in {attempts} attempts!")
else:
    print(f"😞 You've used all your attempts. The number was {number_to_guess}.")
print("-"*30)