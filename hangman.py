# Chapter 10:  Putting it all together w/Hangman!
import random

def hangman(word):
    num_wrong = 0
    guesses = []
    stages = ["",
              "__________          ",
              "|         |         ",
              "|         O         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   ",
              "|                   "
              ]
    rletters = list(word)
    board = ["__"]*len(word)
    win = False
    print("Welcome to Hangman!")
    print("\nThe word has "+str(len(word))+" letters.")

    while num_wrong < len(stages) - 1:
        message = "\nGuess a letter: "
        guess = input(message)
        if guess in guesses:
            print("You already guessed that!")
            continue
        elif guess in rletters:
            for i, letter in enumerate(rletters):
                if guess == letter:
                    rletters[i] = guess
                    board[i] = guess
        else:
            num_wrong += 1
        guesses.append(guess)
        print((" ".join(board)))
        e = num_wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("\nYou win! The word was:",str(word))
            win = True
            break
    if not win:
        print("\nYou lost! Wah wahhh.")
        print("The word was:",word)

words = ["cat",
         "dog",
         "testicle",
         "cuticle",
         "jazz"]

hangman(words[random.randint(0,len(words)-1)])
