import random, sys, time
from os import system, name
from time import sleep
import pygame

pygame.init()

wordlist = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buzzard", "buzzing", "buzzwords", "cobweb", "croquet", "crypt", "cycle", "dizzying", "duplex", "dwarves", "embezzle", "equip", "espionage", "faking", "fishhook", "fixable", "fjord", "flapjack", "flopping", "fluffiness", "foxglove", "frazzled", "fuchsia", "funny", "galaxy", "galvanize", "gazebo", "gizmo", "glowworm", "glyph", "gnostic", "gossip", "grogginess", "haiku", "haphazard", "hyphen", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki", "kilobyte", "kiosk", "kitsch", "kiwi", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph", "marquis", "matrix", "megahertz", "microwave", "mystify", "nightclub", "nowadays", "numbskull", "nymph", "onyx", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel", "pizazz", "pneumonia", "polka", "psyche", "puppy", "puzzling", "quartz", "queue", "quips", "quiz", "quizzes", "quorum", "rhubarb", "rhythm", "rickshaw", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "stretch", "stronghold", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "twelfth", "unknown", "unworthy", "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "walkway", "waltz", "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft", "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yacht", "yippee", "yoked", "youthful", "yummy", "zephyr", "zigzag", "zigzagging", "zipper", "zodiac", "zombie", "peanut butter", "boy scouts", "no one", "ice cream", "real estate", "high school", "living room", "coffee table", "sweet tooth", "grand jury", "post office", "full moon", "half sister", "cave in", "vice president", "blood pressure", "check-in", "half-baked", "merry-go-round", "I failed my way to success", "french fries", "margherita", "tequila", "front desk", "transatlantic", "airtraffic control", "caramel doulche", "vegetarian lasagna", "substitute", "sagittarius", "statistics", "news station", "volkswagen", "cherish", "protruding", "dorm room", "oval office", "constitutional", "the quick brown fox jumps over the lazy dog", "exhibition", "paintbrush", "enchanted castle", "thunderstorm", "apartment complex", "pumpkin spice latte", "rasberry snowcone", "blackberry bush", "lushious forest trees", "massachusetts", "albuquerque new mexico", "costa rican tucans", "computer sleeve", "acrylic paint", "stitches"]

def playSound(filename):
  pygame.mixer.music.load(filename)
  pygame.mixer.music.play()

def slowprint(string): #prints like typing
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    playSound('typekey.wav')
    time.sleep(0.1)

def get_word():
  word = random.choice(wordlist) # chooses random word
  return word.upper() # converts to upper case

def play(word):
  #wordCompletion = "_" * len(word) # an underscore for each letter
  system('cls')
  guessed = False 
  guessed_letters = [] # list for guessed letters
  guessed_words = [] # list for guessed words
  tries = 6 # number of chances

  wordCompletion = ""
  for letter in word:
    if letter == " ":
      wordCompletion += "  "
    elif letter == "-":
      wordCompletion += "- "
    elif letter in guessed_letters:
      wordCompletion += (letter + " ")
    else:
      wordCompletion += "_ "

  # prints the hangman and letters or blanks in the word
  slowprint("H A N G M A N")
  time.sleep(0.7)
  print(showHangman(tries))
  print(wordCompletion)
  print("\n")
  while not guessed and tries > 0:
    guess = input("Please guess a letter or word: ").upper()
    # code for guessing a letter
    if len(guess) == 1 and guess.isalpha(): # checks if input is 1 character long and in alphabet
      if guess in guessed_letters:
        print("You already guessed "+guess+". Try again!")
      elif guess not in word:
        print(guess, "is not in the word.")
        playSound('wrongletter.wav')
        tries -= 1 # removes one chance
        guessed_letters.append(guess) # adds guess to guessed_letters
      else:
        print(guess, "is in the word!")
        playSound('correctletter.wav')
        guessed_letters.append(guess)
        wordCompletion = ""
        for letter in word:
          if letter == " ":
            wordCompletion += "  "
          elif letter == "-":
            wordCompletion += "- "
          elif letter in guessed_letters:
            wordCompletion += (letter + " ")
          else:
            wordCompletion += "_ "
        if "_" not in wordCompletion: # if no more blanks, then word has been guessed
          guessed = True
    # code for guessing a word
    elif len(guess) == len(word): # checks if input is a word and has letters
      if guess in guessed_words:
        print("You already guessed "+guess+".")
      elif guess != word:
        print(guess, "is not the word.")
        playSound('wrongletter.wav')
        tries -= 1
        guessed_words.append(guess)
      else:
        guessed = True
        wordCompletion = word
        print("The word was "+word+"!")
        playSound('wingame.wav')
    else:
      print("Not a valid guess; try again.")

    print(showHangman(tries))
    print(wordCompletion)
    print()
    print("Guessed letters:", guessed_letters)
    if guessed_words != []:
      print("Guessed words:", guessed_words)
    print("\n")
  if guessed:
    print("Congrats, you win!")
    playSound('wingame.wav')
  else: 
    print("You lose! The word was "+word+". Maybe next time!")
    playSound('losegame.wav')

# hangman images
def showHangman(tries):
    stages = [  # lose
                """
                   +——————+
                   │      |
                   │      O
                   │     \\|/
                   │      |
                   │     / \\
                   ┴
                """,
                # 1
                """
                   +——————+
                   │      |
                   │      O
                   │     \\|/
                   │      |
                   │     / 
                   ┴
                """,
                # 2
                """
                   +——————+
                   │      |
                   │      O
                   │     \\|/
                   │      |
                   │     
                   ┴
                """,
                # 3
                """
                   +——————+
                   │      |
                   │      O
                   │     \\|
                   │      |
                   │     
                   ┴
                """,
                # 4
                """
                   +——————+
                   │      |
                   │      O
                   │      |
                   │      |
                   │     
                   ┴
                """,
                # 5
                """
                   +——————+
                   │      |
                   │      O
                   │     
                   │     
                   │     
                   ┴
                """,
                # 6
                """
                   +——————+
                   │      │
                   │      
                   │    
                   │      
                   │     
                   ┴
                """
    ]
    return stages[tries]

# code to run the game
def main():
  word = get_word()
  play(word)
  # code to play again
  while input("Play again? (Y/N) ").upper() == "Y":
    word = get_word()
    play(word)
    

main()
