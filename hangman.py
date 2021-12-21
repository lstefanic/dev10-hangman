import random
import math

def choose_word():
    # stuff
    f = open("words.txt")
    words = f.read().splitlines()
    f.close()
    index = math.floor(random.random() * len(words))
    return words[index]

def display_info(secret_word,guessed_letters,num_guesses):

    revealed = "\n    Secret word: "
    for i in range(len(secret_word)):
        if ( secret_word[i] in guessed_letters ):
            revealed += secret_word[i]
        else:
            revealed += "_"
        revealed += " "
    print(revealed[0:-1])

    guessed = "    Guessed letters: "
    for letter in sorted(guessed_letters):
        guessed += letter + " "
    print(guessed[0:-1])

    print("    Remaining guesses: %u\n" % num_guesses)

def get_guess():

    guess = "1"
    while ( not guess.isalpha() ):
        guess = input("Guess a letter or the entire word: ")
    return guess.lower()

def play_once(secret_word):

    num_guesses = 7
    guessed_letters = set()

    while ( num_guesses > 0 ):
        display_info(secret_word,guessed_letters,num_guesses)
        guess = get_guess()
        if ( len(guess) > 1 ):
            if ( guess == secret_word ):
                print("\n    You win!")
                return 1
            else:
                num_guesses -= 1
        else:
            guessed_letters.add(guess)
            if ( secret_word.find(guess) == -1 ):
                num_guesses -= 1

    print("\n    You lose, the word was %s" % secret_word)
    return 0

games_played = 0
wins = 0
used_words = set()
play_again = "y"
while ( play_again == "y" ):
    games_played += 1
    secret_word = choose_word()
    while (secret_word in used_words ):
        secret_word = choose_word()
    used_words.add(secret_word)
    wins += play_once(secret_word)
    print("    %u wins, %u losses\n" % (wins, games_played - wins))
    play_again = input("Play again? (y/n): ")