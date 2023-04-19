import random
import requests

# Constants here 
VALID_WORDS = ['tests', 'others', "halloweens", "series", "accomplices", "shows"]
MAX_NUMBER_OF_GUESSES = 6

# ex: keep track of user's inputs, potential list of words to choose from, etc...
USERS_INPUTS = []

# Pick a word for hangman round
def pick_word():
    url = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.request("GET", url)
    p = response.text
    y = p.splitlines()
    r = random.sample(y, 2)
    while len(r[0]) < 5:
        r[0] = random.choice(y)
    while len(r[1]) < 5:
        r[1] = random.choice(y)
    return r[0], r[1]

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
            '  |      \n'
            '  |      \n'
            '  |      \n'
            '  |      \n'
            '__|__\n')
    elif counter == 2:
         print('   _____ \n'
            '  |     | \n'
            '  |     | \n'
            '  |      \n'
            '  |      \n'
            '  |      \n'
            '  |      \n'
            '__|__\n')
    elif counter == 3:
        print('   _____ \n'
            '  |     | \n'
            '  |     | \n'
            '  |     | \n'
            '  |      \n'
            '  |      \n'
            '  |      \n'
            '__|__\n')
    elif counter == 4:
        print('   _____ \n'
            '  |     | \n'
            '  |     | \n'
            '  |     | \n'
            '  |     O \n'
            '  |      \n'
            '  |      \n'
            '__|__\n')
    elif counter == 5:
        print('   _____ \n'
            '  |     | \n'
            '  |     | \n'
            '  |     | \n'
            '  |     O \n'
            '  |     | \n'
            '  |      \n'
            '__|__\n')
    elif counter == 6:
        print('   _____ \n'
            '  |     | \n'
            '  |     | \n'
            '  |     | \n'
            '  |     O \n'
            '  |    /|\ \n'
            '  |      \n'
            '__|__\n')
    elif counter == 7:
        print('   _____ \n'
                '  |     | \n'
                '  |     | \n'
                '  |     | \n'
                '  |     O \n'
                '  |    /|\ \n'
                '  |    / \ \n'
                '__|__\n')
        

# Create a function to take the user's inputs (letters)
def accept_letter(r, s):
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


#This draws the underscores and replaces them once a letter is correctly guessed. Ex: t _ _ s _ _
def print_answer(r, s):
    c = "" + " " + ""
    for x in r:
        if x in USERS_INPUTS:
            c += x 
        else:  
            c += "_" 
    c += "\t"
    for x in s:
        if x in USERS_INPUTS:
            c += x 
        else:
            c += "_"
    print(c)


# Checks if the answer/input is correct 
def check_answer(r, s):
    missing_word = True
    missing_word2 = True 
    for x in r:
        if x not in USERS_INPUTS:
            missing_word = False         
    for x in s:
        if x not in USERS_INPUTS:
            missing_word2 = False
    return missing_word, missing_word2


# What actually runs when we use "python3 Hangman.py"
if __name__ == '__main__': 
    r, s = pick_word()
    counter = 0 
    print("Starting hangman script!")
    first, second = check_answer(r, s)
    while first is False or second is False:
        if accept_letter(r, s) == False:
            counter += 1 
        draw_guillotine(counter)
        if counter == 7:
            print("You Lost")
            break 
        print_answer(r, s)
        first, second = check_answer(r, s)
        print(counter)
    if first and second is True:
        print("Congrats! You won!")
    print("Words:", r, s)


