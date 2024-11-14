import random

# List of words related to Computer Science
words = ["algorithm", "function", "variable", "compile", "iterate", 
         "recursion", "binary", "array", "syntax", "pointer"]

def play_game():
    word = random.choice(words)  # Randomly choose a word from the list
    guessed_letters = []  # List to store guessed letters
    incorrect_guesses = 0  # Counter for incorrect guesses
    max_incorrect_guesses = 6  # Maximum incorrect guesses before losing
    lifelines = 1  # Player has 1 lifeline for requesting a hint

    print("Welcome to Hangman!")
    
    # Game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Display header and current word progress
        print("\nHANGMAN")
        print("^" * (incorrect_guesses + 1))  # Pointer moves right with each incorrect guess
        display = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display))  # Show current state of the word
        
        # Check if the player wants a hint
        if lifelines > 0:
            hint_request = input("Do you want a hint? (y/n): ").lower()
            if hint_request == 'y':
                # Provide a hint (first unguessed letter)
                for i, letter in enumerate(word):
                    if letter not in guessed_letters:
                        print(f"Hint: The first missing letter is '{letter}'.")
                        guessed_letters.append(letter)  # Add the hint letter to guessed letters
                        lifelines -= 1  # Deduct one lifeline
                        break
                continue  # Skip the rest of the loop for this turn

        # Get the player's guess
        guess = input("Guess a letter: ").lower()  # Get player's guess

        # Ensure input is a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # If the letter has been guessed already
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)  # Add guessed letter to the list

        # Check if the guess is correct or incorrect
        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            incorrect_guesses += 1  # Increment incorrect guesses

        # Check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: '{word}'")
            print("Phew... you are saved.")
            break
    else:
        # If the player runs out of guesses
        print(f"You are hanged! The word was: '{word}'")

def main():
    while True:
        play_game()  # Play the game
        replay = input("Do you want to play again? (y/n): ").lower()  # Ask to replay
        if replay != 'y':
            print("Thanks for playing! Goodbye.")
            break

# Run the game
if __name__ == "__main__":
    main()
