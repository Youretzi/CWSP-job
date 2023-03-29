import random

# Constants here 
VALID_WORDS = ['test', 'other', "halloween", "series", "accomplice", "show"]
MAX_NUMBER_OF_GUESSES = 6

# ex: keep track of user's inputs, potential list of words to choose from, etc...
USERS_INPUTS = []
r = random.choice(VALID_WORDS)
# Pick a word for hangman round
def pick_word(r):
    #return a word from VALID_WORDS
   
    print(r)
    return r
    pass

# Create a function to draw the guillotine
def draw_guillotine():
    print(  '   _____ \n'
            '  |      \n'
            '  |      \n'
            '  |      \n'
            '  |      \n'
            '  |      \n'
            '  |      \n'
            '__|__\n')
    pass


# Create a function to take the user's inputs (letters)
def accept_letter(r):
    #make sure to reject if user inputs a number or more than one character
    a = input("Guess: ")
    ch = a
    while a.isnumeric() is True:
        a = input("Error, Enter New input: ")
        print(a)
    if len(a) != 1:
        a = input("Error, Enter New input: ")
        print(a)
    elif ch in r: 
        d = input("Correct! Try new input: ")
        print(d)
    else:
        print('   _____ \n'
              '  |     | \n'
              '  |     | \n'
              '  |      \n'
              '  |      \n'
              '  |      \n'
              '  |      \n'
              '__|__\n')
    pass


# Create a function to play out each round
def play_round():
    pass


# What actually runs when we use "python3 Hangman.py"
if __name__ == '__main__':
    print("Starting hangman script!")
    print(pick_word(r))
    print(draw_guillotine())
    print(accept_letter(r))
    print(play_round())

    # pick word
    # draw guillotine with underscores
    # for loop for max guesses
        # take user input
        # redraw hangman
        # check if guessed word is same as picked word
            # if guessed correctly, print you win and exit for loop using 'break'
    # if guessed word not picked word then print game over and print dead hangman
