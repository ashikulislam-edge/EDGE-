def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Set a fixed secret number for the game
    secret_number = 42
    attempts = 3

    while True:
        try:
            # Ask the user for their guess
            guess = int(input("Enter your guess number: "))
            attempts += 1
            
            # Check if the guess is too high, too low, or correct
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()
