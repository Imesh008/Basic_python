import random 

number_to_guess =  random.randint (1, 100)
attemps = 0
diffculty = input ("Choose difficulty (Easy/Medium/Hard): ").lower()
max_attemps = 10 if difficulty == "easy" else 7 if difficulty == "medium" else 5
 

guess = int(input("Guess a number between 1 and 100: "))

while guess != number_to_guess:
    attemps += 1
    if guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    if attemps >= max_attemps:
        break
    guess = int(input("Try again:"))


if guess == number_to_guess:
    print(f"🎉 You guessed it in {attempts} attempts!")

print("Congratulations! You've guessed the number:", number_to_guess)