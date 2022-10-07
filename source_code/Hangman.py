from extend import separate_chars
from extend import list2str
from extend import diffconverter
from center import terminal_width
from center import terminal_height
from words import random_word
from math import ceil
from time import sleep
import os
import colorama

os.system('cls')
width = terminal_width()
height = terminal_height()
print(colorama.Fore.RED + "\n"*(ceil(height / 2)-15) + "Please use fullscreen for best experience.".center(width))
sleep(5)
os.system('cls')

colorama.init()

print(colorama.Fore.GREEN + "\n"*(ceil(height / 2)-4) + "Welcome to:".center(width) + "\n\n" + "██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗".center(width) + "\n" + "██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║".center(width) + "\n" + "███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║".center(width) + "\n" + "██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║".center(width) + "\n" + "██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║".center(width)  + "\n" + "╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝".center(width)  + "\n" + "Creator: Alex J.".center(width))

start_bool = True

while True:
    word = random_word()
    while start_bool == True:
        difficulty = input("\nDifficulty 1 - 3: ")
        
        try:
            diffconverter(int(difficulty))
        except:
            print("Input conversion error, try a number?")
        else:
            difficulty = diffconverter(int(difficulty))

            if difficulty <= 2 and difficulty >= 1:
                print("\nDifficulty set.\nWord set.\nHave fun!")
                start_bool = False
            else:
                print("Difficulty not in range.")


    listed_input = separate_chars(word)
    fill_list = separate_chars("_" * len(listed_input))
    guess_amount = ceil(len(word) * diffconverter(difficulty))
    while_count = 0

    print("\nYou have " + str(guess_amount) + " guesses.")

    for i in range(guess_amount):
        guess_bool = True
        
        while guess_bool == True:
            guess_input = input("\nGuess: ")
            guess = guess_input.lower()
            alphabet = "a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z".split('/')

            try:
                alphabet.index(guess)
            except:
                if len(guess) > 1:
                    print("Guess has too many characters.")
                else:
                    print("Guess is not a letter, try again.")
            else:
                guess_bool = False

        guess_num = 0
        while_count = while_count + 1

        for i in range(listed_input.count(guess)):
            # print("in: " + str(listed_input)) <-- for testing purposes
            
            fill_list[listed_input.index(guess)] = guess
            listed_input[listed_input.index(guess)] = "_"
            guess_num = guess_num + 1

        print("\n" + list2str(fill_list))

        if guess_amount - while_count == 1:
            a = " guess"
        else:
            a = " guesses"

        if guess_num == 0:
            print("No " + guess + "'s found. ;w;  " + str(guess_amount - while_count) + a + " left.\n")

        if guess_num == 1:
            print("1 " + guess + " found! " + str(guess_amount - while_count) + a + " left.\n")

        if guess_num > 1:
            print(str(guess_num) + " " + guess + "'s found! " + str(guess_amount - while_count) + a + " left.\n")

        if fill_list == separate_chars(word):
            print("Congrats, you win!")
            break

        if guess_amount - while_count == 0:
            print("You lose. I am crying.\nWord was: " + word + "\n")
            break
    
    play = input("Would you like to play again (y/n)? ")

    if play == "n":
        print("Thanks for playing!" + colorama.Fore.RESET)
        break
    elif play == "y":
        print("\nAlright, let's play again!\n")
    elif play != "y" and play != "n":
        print("Not y or n, continuing anyways.")
    os.system('cls')