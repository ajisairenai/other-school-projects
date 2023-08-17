# Written by Hydreesia

import random
import display_utility
import wordle
from words import words

def filter_word_list(words, clues):
    """
    Purpose:
        filters a word list passed into it to show 
    Parameter(s):
        words: a list of words
        clues: a list of tuples, each tuple being a guess (string) and clues returned (a list of strings)
    Return Value:
        a new word list containing only the words in the input word list which could be the secret word
    """
    filtered = []

    for word in words:
        filter_clues = []
        for ele in clues:
            filter_clues.append((ele[0].upper(), wordle.check_word(word.upper(), ele[0])))
        if filter_clues == clues:
            filtered.append(word)
    return filtered

def easy_wordle():
    """
    A function to play wordle
    """
    secret = random.choice(words)
    game = True
    clues = []
    count = 0

    while game:
        guess = input("> ")
        while (not guess.islower()) or (len(guess) != 5) or (guess not in words):
            guess = input("> ")
        count += 1

        check_list = wordle.check_word(secret, guess)
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
        
        filtered = filter_word_list(words, clues)
        print(len(filtered), "words possible:")
        random.shuffle(filtered)
        for word in filtered[:5]:
            print(word)

        if check_list.count('green') == 5 or count == 6:
            print("Answer:", secret.upper())
            game = False

if __name__ == '__main__':
    easy_wordle()