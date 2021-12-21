import random
import math

def choose_word():
    # stuff
    f = open("words.txt")
    words = f.read().splitlines()
    f.close()
    index = math.floor(random.random() * len(words))
    return words[index]

def display_revealed_letters(SECRET_WORD,guessed_letters):

    revealed = "Secret word: "
    for i in range(len(SECRET_WORD)):
        if ( SECRET_WORD[i] in guessed_letters ):
            revealed += SECRET_WORD[i]
        else:
            revealed += "_"
    print(revealed)

def get_guess():

    guess = "1"
    while ( not guess.isalpha() ):
        guess = input("Guess a letter or the entire word: ")
    return guess.lower()

def play():

    SECRET_WORD = choose_word()
    num_guesses = 7
    guessed_letters = set()

    while ( num_guesses > 0 ):
        display_revealed_letters(SECRET_WORD,guessed_letters)
        guess = get_guess()
        if ( len(guess) > 1 ):
            if ( guess == SECRET_WORD ):
                print("You win!")
                return
            else:
                num_guesses -= 1
        else:
            if ( SECRET_WORD.find(guess) != -1 ):
                guessed_letters.add(guess)
            else:
                num_guesses -= 1

    print("You lose")

play()