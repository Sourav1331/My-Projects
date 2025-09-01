import random
print("\n::::  Welcome to number guessing game  ::::\n")

limit = random.randint(5, 10)
n = random.randint(0, 30)

print(f"You have maximum {limit} number of guesses allowed")

guess = 0

while (guess < limit):
    while True:
        b = input(f"Guess the number between 0 to 30: ").strip()
        if not b:
            print("Enter a number. Don't left the space empty!")
            continue
        try:
            a = int(b)
            break
        except ValueError:
            print("Invalid input!")

    guess += 1
    if(a < n):
        print("Think of a higher number!")
        print(f"You have {limit - guess} guesses left\n")

    elif(a > n):
        print("Think of a lower number!")
        print(f"You have {limit - guess} guesses left\n")

    else:    
        print(f"You have guessed the correct number {n} in {guess} guesses.")
        print("Thanks for playing...")
        break
else:
    print(f"Oh....You have reached the limit.\nThe correct number was {n}")
