import random

# Constants here 
VALID_WORDS = ['tests', 'others', "halloweens", "series", "accomplices", "shows"]
MAX_NUMBER_OF_GUESSES = 6

# ex: keep track of user's inputs, potential list of words to choose from, etc...
USERS_INPUTS = ["s"]
# Pick a word for hangman round
def pick_word():
    #return a word from VALID_WORDS
    r = random.choice(VALID_WORDS)
    print(r)
    return r
    pass

# Create a function to draw the guillotine
def draw_guillotine(counter):
    if counter == 0:
        print(  '   _____ \n'
                '  |      \n'
                '  |      \n'
                '  |      \n'
                '  |      \n'
                '  |      \n'
                '  |      \n'
                '__|__\n')   
    elif counter == 1:  
        print('   _____ \n'
            '  |     | \n'
            '  |     | \n'
            '  |      \n'
            '  |      \n'
            '  |      \n'
            '  |      \n'
            '__|__\n')
    elif counter == 2:
        print('   _____ \n'
            '  |     | \n'
            '  |     | \n'
            '  |     | \n'
            '  |      \n'
            '  |      \n'
            '  |      \n'
            '__|__\n')
    elif counter == 3:
        print('   _____ \n'
            '  |     | \n'
            '  |     | \n'
            '  |     | \n'
            '  |     O \n'
            '  |      \n'
            '  |      \n'
            '__|__\n')
    elif counter == 4:
        print('   _____ \n'
                '  |     | \n'
                '  |     | \n'
                '  |     | \n'
                '  |     O \n'
                '  |    /|\ \n'
                '  |    / \ \n'
                '__|__\n')
        
    


# Create a function to take the user's inputs (letters)
def accept_letter(r):
    #make sure to reject if user inputs a number or more than one character
    while True:
        a = input("Guess: ")
        ch = a
        if a.isnumeric() is True:
             print("Error, No numbers in input")
        elif len(a) != 1:
            print("Error input must be one character")   
        elif a.lower() in USERS_INPUTS:
            print("This letter has been gussed")
        elif ch in r:
            USERS_INPUTS.append(a.lower())
            print("Correct, guess again: ")
            return True
        else:
            print("letter not in word")
            USERS_INPUTS.append(ch)
            return False 
def print_answer(r):
    c = ""
    for x in r:
        if x in USERS_INPUTS:
            c += x 
        else: 
            c += "_"
    print (c)

# Create a function to play out each round
def play_round():
    pass

def check_answer(r):
    missing_word = True
    for x in r:
        if x not in USERS_INPUTS:
            missing_word = False
    return missing_word


# What actually runs when we use "python3 Hangman.py"
if __name__ == '__main__': 
    r = pick_word()
    counter = 0 
    print("Starting hangman script!")
    while check_answer(r) is False:
        if accept_letter(r) == False:
            counter += 1 
        draw_guillotine(counter)
        if counter == 4:
            print("You Lost")
            break 
        print_answer(r)
        #print(play_round())
        check_answer(r)
        print(counter)
    if check_answer(r) is True:
        print("Congrats! You won!")
    # pick word
    # draw guillotine with underscores
    # for loop for max guesses
        # take user input
        # redraw hangman
        # check if guessed word is same as picked word
            # if guessed correctly, print you win and exit for loop using 'break'
    # if guessed word not picked word then print game over and print dead hangman
