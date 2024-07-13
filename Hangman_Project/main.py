import stages
import random
import csv

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = pick_random_word("words")
wordList = []
for x in word:
    wordList.append("_")

def mainmenu():
    print("Welcome To the Hangman Game")
    print("You have 5 lives in this game")
    print("Each Turn You have to guess ONE letter")
    print("You can only guess a letter once")
    print("**********************************")
    print("Please guess your first letter")
    printWord()

def pick_random_word(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
        words = [word.strip(',') for word in words]  # Remove trailing commas
        return random.choice(words)


def guess():
    letter = input()
    if lettercheck(letter):
        wordCheck()
    else:
        print("Inavlid Input")
        print("Please enter a new letter")
        guess()

def lettercheck(letter):
    if len(letter) == 1:
        letter = letter.lower()
        for x in alphabet:
            if x == letter:
                alphabet.remove(x)
                return True 
    return False