### This code displays a Python version of the classic-word guessing game, Hangman. 
### The object of the game is to guess letters until the secret word has been correctly guessed. 
### The player has 6 attempts before the full body of the man is hung, and the game is over.

### Imports random module, which includes random number generation-related functions.
import random

### Contains art strings that represent different stages of the Hangman.
hangman1 = [
"""
+---+
    |
    |
    |
    ===""", """
+---+
  | |
  O |
    |
    ===""", """
+---+
  | |
  O |
 /| |
    ===""", """
+---+
  | |
  O |
 /|\|
    ===""", """
+---+
  | |
  O |
 /|\|
  |  ===""", """
 / 
+---+
  | |
  O |
 /|\|
  |  ===""", """
 / \
"""
]

### Creates a list of words for the user to guess from. To simplify the game, I chose to use the colors of the rainbow. 
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

### Tells the program to select a random word from the (colors) list, and convert them to lowercase letters.
word = random.choice(colors).lower()

### Stores correctly and incorrectly guessed letters.
guessed_correctly = []
guessed_incorrectly = []

### Defines number of attempts allowed and subtracts 1 after each incorrect guess. 
tries = 6
hangman_count = -1

### Introduces the game to the user, and gives instuctions + the category for the game.
print("Welcome to Hangman!")
print("Please guess letters one at a time to decipher the secret word. The category is: colors of the rainbow.")

### Controls the game flow based on the remaining attempts. 
### If-else statements determine the correctness of the guessed letters, providing feedback
### after correct and incorrect guesses.
while tries > 0:
    output = ''
    for letter in word:
        if letter in guessed_correctly:
            output += letter
        else:
            output += '_ '
    if output == word:
        break
    print("Guess a letter: ",output)
    print(tries," attempts remaining")
    guess = input().lower()
    if guess in guessed_correctly or guess in guessed_incorrectly:
        print("You've already guessed", guess)
    elif guess in word:
        print("Great Job! You guessed the letter correctly!")
        guessed_correctly.append(guess)
    else:
        print("Sorry! You guessed the letter incorrectly!")
        hangman_count = hangman_count + 1
        tries = tries-1
        guessed_incorrectly.append(guess)
        print(hangman1[hangman_count])

### Lets the user know whether they have won or lost the game. 
if tries>0:
    print("Congratulations! You won!")
else:
    print("You lost. Game over.")
