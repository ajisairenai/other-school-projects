# Written by Hydreesia

import random
import display_utility
from words import words

def check_word(secret, guess):
    """
    Purpose:
        Check if the guess is correct.
    Parameter(s):
        secret: a string, the secret word
        guess: a string, the guess
    Return Value:
        a 5-length list containing "grey", "yellow", and "green" as clues for the secret word
    """
    clues = ["grey", "grey", "grey", "grey", "grey"]
    used_idx = []

    # checks for green first
    for i, letter in enumerate(guess):
        if letter == secret[i]:
            clues[i] = "green"
            used_idx.append(i)

    # checks for yellow
    for i, letter in enumerate(guess):
        # ignores anything that is already green
        if clues[i] == "green":
            continue
        else:
            if letter in secret:
                j = secret.find(letter)
                while j in used_idx:
                    j = secret.find(letter, j+1)
                if j != -1:
                    clues[i] = "yellow"
                    used_idx.append(j)
    return clues

def known_word(clues):
    """
    Purpose: 
        helps with basic record keeping for the end-user by showing what is known about the word so far
    Parameter(s):
        clues: a list of tuples, each tuple being a guess (string) and clues returned (a list of strings)
    Return Value:
        a string indicating what we know about the secret word according to green hints seen so-far
    """
    # clues tuples are in the format (guess, clue)
    known = ['_', '_', '_', '_', '_']

    for ele in clues:
        for i in range(5):
            if ele[1][i] == 'green':
                known[i] = ele[0][i].upper()
    known = "".join(known)
    return known

def no_letters(clues):
    """
    Purpose:
        helps with basic record keeping for the end-user by showing what letters are not in the word
    Parameter(s):
        clues: a list of tuples, each tuple being a guess (string) and clues returned (a list of strings)
    Return Value:
        a string of all letters that are not in the word in alphabetic order
    """
    no_letters = []
    for ele in clues:
        for i in range(5):
            if (ele[1][i] == 'grey') and (ele[0][i] not in no_letters):
                no_letters.append(ele[0][i])
    
    no_letters_copy = no_letters[:]
    for letter in no_letters:
        for i in range(len(clues)):
            for j in range(5):
                if (letter == clues[i][0][j]) and (clues[i][1][j] != 'grey') and (letter in no_letters_copy):
                    no_letters_copy.remove(letter)
                    
    
    return (''.join(sorted(no_letters_copy))).upper()

def yes_letters(clues):
    """
    Purpose:
        helps with basic record keeping for the end-user by showing what letters are in the word
    Parameter(s):
        clues: a list of tuples, each tuple being a guess (string) and clues returned (a list of strings)
    Return Value:
        a string of all letters that are in the word in alphabetic order
    """
    yes_letters = []

    for ele in clues:
        for i in range(5):
            if (ele[1][i] == 'green' or ele[1][i] == 'yellow') and (ele[0][i] not in yes_letters):
                yes_letters.append(ele[0][i])
    return (''.join(sorted(yes_letters))).upper()

def wordle():
    """
    A function to play wordle
    """
    secret = random.choice(words)
    game = True
    clues = []
    count = 0

    while game:
        print("Known:", known_word(clues))
        print("Green/Yellow Letters:", yes_letters(clues))
        print("Grey Letters:", no_letters(clues))

        guess = input("> ")
        while (not guess.islower()) or (len(guess) != 5) or (guess not in words):
            guess = input("> ")
        count += 1

        check_list = check_word(secret, guess)
        clues.append((guess.upper(), check_list))
        for ele in clues:
            for i in range(5):
                if ele[1][i] == 'green':
                    display_utility.green(ele[0][i].upper())
                elif ele[1][i] == 'yellow':
                    display_utility.yellow(ele[0][i].upper())
                else:
                    display_utility.grey(ele[0][i].upper())
            print()

        if check_list.count('green') == 5 or count == 6:
            print("Answer:", secret.upper())
            game = False

if __name__ == "__main__":
    wordle()