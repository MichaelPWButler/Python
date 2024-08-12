import random
import csv

# Creating starting variables that store the number of lives and each letter of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lives = 5

# Simple main menu function that is the first thing shown to the user when they start the game
def mainmenu():
    print("Welcome To the Hangman Game")
    print("You have 5 lives in this game")
    print("Each Turn You have to guess ONE letter")
    print("You can only guess a letter once")
    guess(lives, alphabet)

# A small function that prints out the current state of the word being guessed all in one line
def printWord():
    print(*wordList)

# A function that opens the text file that stores all the words a picks a random one for each game
def pick_random_word(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
        words = [word.strip(',') for word in words]  # Remove trailing commas
        return random.choice(words)

# The main function that gets the user to guess a letter and then checks that letter
def guess(lives, alphabet):
    print("**********************************")
    printWord()
    print("**********************************")
    print("Please enter your letter you are guessing:")
    letter = input()
    # This checks if the user entered a single letter, if it has not already been guessed and if it is in the correct word
    if lettercheck(letter, alphabet) == False or wordCheck(letter) == False:
        lives = lives - 1
        print("You have lost a life, you now have", lives ,"lives left")
    
    # the function then ends by checking if the game should ginish or not based on the last guess
    gameOver(lives, alphabet)

# This function check the letter, checks it is a valid letter and then checks it has not already been guessed, if valid and not guessed it removes it from the avilable letters to guess 
def lettercheck(letter, alphabet):
    if len(letter) == 1:
        letter = letter.lower()
        for x in alphabet:
            if x == letter:
                alphabet.remove(x)
                return True 
    return False

# This function checks if the letter is in the correct word and then chnages the list to show the correct letters
def wordCheck(letter):
    if letter not in word:
        return False
    else:
        for x in range(len(word)):
            if word[x] == letter:
                wordList[x] = letter
    
# This function is checking if the game should finish, either by no more lives or the full word has been guessed
def gameOver(lives, alphabet):
    if lives == 0:
        print("Game Over you have run out of lives")
        print("The word was", word)
    elif "_" not in wordList:
        print("Congratulations you have won")
        print("The word was", word)
    else:
        guess(lives, alphabet)

# This small section of the program generators the random word and then converts that word into a list storing each individual letter
word = pick_random_word("words.txt")
wordList = []
for x in word:
    wordList.append("_")

mainmenu()