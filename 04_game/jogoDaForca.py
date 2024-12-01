# Hangman Game - Code with Variables in English

# Importing libraries
import random
from os import system, name

# Function to clear the screen
def clear_screen():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac or Linux
    else:
        _ = system('clear')

# Function to display the hangman
def display_hangman(attempts):
    # List of hangman stages
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[attempts]

# Main game function
def game():
    clear_screen()
    print("\nWelcome to the Hangman Game :)")
    print("Guess the word below:\n")
    
    # List of words
    words = ['morango', 'melancia', 'groselha', 'mirtilo', 'framboesa']
    
    # Choosing a random word
    chosen_word = random.choice(words)
    
    # List of letters in the word
    word_letters = [letter for letter in chosen_word]
    
    # Initial board
    board = ["_"] * len(chosen_word)
    
    # Number of attempts
    attempts = 6
    
    # List of wrong guesses
    wrong_guesses = []
    
    # Game loop
    while attempts > 0:
        print(display_hangman(attempts))
        print("\nWord: ", " ".join(board))
        print("Wrong Guesses: ", " ".join(wrong_guesses))
        
        # Player's input
        guess = input("\nEnter a letter: ").lower()
        
        # Validating guess
        if guess in wrong_guesses or guess in board:
            print("\nYou already guessed that letter. Try another.")
            continue
        
        # Checking the guess
        if guess in word_letters:
            print("\nYou guessed a correct letter!")
            for index in range(len(word_letters)):
                if word_letters[index] == guess:
                    board[index] = guess
            if "_" not in board:
                print("\nCongratulations! You won! The word was: {}".format(chosen_word))
                break
        else:
            print("\nThat letter is not in the word.")
            attempts -= 1
            wrong_guesses.append(guess)
    
    # Losing condition
    if "_" in board:
        print("\nYou lost! The word was: {}.".format(chosen_word))

# Main block
if __name__ == "__main__":
    game()
    print("\nWell done on completing the game! Keep learning Python!")
