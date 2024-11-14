import random
from colorama import init, Fore
from time import sleep

# Initialize colorama
init(autoreset=True)

# List of words related to Computer Science
words = ["algorithm", "function", "variable", "compile", "iterate", 
         "recursion", "binary", "array", "syntax", "pointer"]

# Hangman stages (ASCII art)
HANGMAN_STAGES = [
    '''
     ------
     |    |
          |
          |
          |
          |
    ========
    ''',
    '''
     ------
     |    |
     O    |
          |
          |
          |
    ========
    ''',
    '''
     ------
     |    |
     O    |
     |    |
          |
          |
    ========
    ''',
    '''
     ------
     |    |
     O    |
    /|    |
          |
          |
    ========
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    ========
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    ========
    ''',
    '''
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    ========
    '''
]

def play_game():
    word = random.choice(words)  # Randomly choose a word from the list
    guessed_letters = []  # List to store guessed letters
    incorrect_guesses = 0  # Counter for incorrect guesses
    max_incorrect_guesses = 6  # Maximum total guesses (incorrect + hint usages)

    print(Fore.CYAN + "Welcome to Hangman!\n")

    # Game loop
    while incorrect_guesses < max_incorrect_guesses:
        # Display the hangman state
        print(HANGMAN_STAGES[incorrect_guesses])
        
        # Display current word progress
        display = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display))  # Show current state of the word

        # Allow the player to request a hint (counts as one incorrect guess)
        if incorrect_guesses < max_incorrect_guesses:
            hint_request = input(Fore.YELLOW + "Do you want a hint? (y/n): ").lower()
            if hint_request == 'y':
                # Provide a hint (first unguessed letter)
                for i, letter in enumerate(word):
                    if letter not in guessed_letters:
                        print(Fore.MAGENTA + f"Hint: The first missing letter is '{letter}'.")
                        guessed_letters.append(letter)  # Add the hint letter to guessed letters
                        incorrect_guesses += 1  # Deduct one chance for the hint
                        break
                continue  # Skip the rest of the loop for this turn

        # Get the player's guess
        guess = input(Fore.GREEN + "Guess a letter: ").lower()  # Get player's guess

        # Ensure input is a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print(Fore.RED + "Please enter a single letter.")
            continue

        # If the letter has been guessed already
        if guess in guessed_letters:
            print(Fore.YELLOW + "You already guessed that letter.")
            continue

        guessed_letters.append(guess)  # Add guessed letter to the list

        # Check if the guess is correct or incorrect
        if guess in word:
            print(Fore.GREEN + "Good guess!")
        else:
            print(Fore.RED + "Wrong guess!")
            incorrect_guesses += 1  # Increment incorrect guesses or hint usage

        # Check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print(Fore.GREEN + f"Congratulations! You guessed the word: '{word}'")
            print(Fore.GREEN + "Phew... you are saved.")
            break
    else:
        # If the player runs out of chances (incorrect guesses + hint usages)
        print(HANGMAN_STAGES[incorrect_guesses])  # Show the last stage
        print(Fore.RED + f"You are hanged! The word was: '{word}'")

def main():
    while True:
        play_game()  # Play the game
        replay = input(Fore.YELLOW + "Do you want to play again? (y/n): ").lower()  # Ask to replay
        if replay != 'y':
            print(Fore.CYAN + "Thanks for playing! Goodbye.")
            break

# Run the game
if __name__ == "__main__":
    main()
