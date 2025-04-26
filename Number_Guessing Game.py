import random

print("Hi, welcome to the game! This is a number guessing game.")
print("You have 7 chances to guess the number. Let's start the game!\n")

number_to_guess = random.randrange(200)
max_chances = 7
guessed_count = 0

while guessed_count < max_chances:
    guessed_count += 1
    try:
        guess = int(input(f"Attempt {guessed_count}: Guess the number: "))
    except ValueError:
        print("Invalid input! Please enter an integer number.")
        guessed_count -= 1  # Don't count invalid attempts
        continue

    difference = abs(number_to_guess - guess)

    if guess == number_to_guess:
        print(f"🎉 Congratulations! You guessed the number {number_to_guess} correctly!")
        break
    elif guessed_count >= max_chances:
        print(f"😔 Oops, you've used all your chances. The number was {number_to_guess}. Better luck next time!")
        break
    else:
        if difference <= 5:
            print("🔥 Very close! You're within 5 numbers. Try again!")
        elif difference <= 10:
            print("👍 Close! You're within 10 numbers. Try again!")
        else:
            print("❄️ You're far from the number. Try again!")

        if guess < number_to_guess:
            print("Hint: Your guess is **too low**.\n")
        else:
            print("Hint: Your guess is **too high**.\n")
