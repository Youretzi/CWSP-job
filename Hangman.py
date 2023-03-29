import random

# Constants here 
VALID_WORDS = ['TEST', 'OTHER']
MAX_NUMBER_OF_GUESSES = 6

# ex: keep track of user's inputs, potential list of words to choose from, etc...
USERS_INPUTS = []


# Pick a word for hangman round
def pick_word():
    #return a word from VALID_WORDS
    pass


# Create a function to draw the guillotine
def draw_guillotine():
    pass


# Create a function to take the user's inputs (letters)
def accept_letter():
    #make sure to reject if user inputs a number or more than one character
    pass


# Create a function to play out each round
def play_round():
    pass


# What actually runs when we use "python3 Hangman.py"
if __name__ == '__main__':
    print("Starting hangman script!")

    # pick word
    # draw guillotine with underscores
    # for loop for max guesses
        # take user input
        # redraw hangman
        # check if guessed word is same as picked word
            # if guessed correctly, print you win and exit for loop using 'break'
    # if guessed word not picked word then print game over and print dead hangman

