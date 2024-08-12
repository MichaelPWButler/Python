import random
import csv

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lives = 5

def mainmenu():
    print("Welcome To the Hangman Game")
    print("You have 5 lives in this game")
    print("Each Turn You have to guess ONE letter")
    print("You can only guess a letter once")
    guess(lives, alphabet)

    

def printWord():
    print(*wordList)

def pick_random_word(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
        words = [word.strip(',') for word in words]  # Remove trailing commas
        return random.choice(words)


def guess(lives, alphabet):
    print("**********************************")
    printWord()
    print("**********************************")
    print("Please enter your letter you are guessing:")
    letter = input()
    if lettercheck(letter, alphabet) == False or wordCheck(letter) == False:
        lives = lives - 1
        print("You have lost a life, you now have", lives ,"lives left")
    
    gameOver(lives, alphabet)

def lettercheck(letter, alphabet):
    if len(letter) == 1:
        letter = letter.lower()
        for x in alphabet:
            if x == letter:
                alphabet.remove(x)
                return True 
    return False

def wordCheck(letter):
    if letter not in word:
        return False
    else:
        for x in range(len(word)):
            if word[x] == letter:
                wordList[x] = letter
    
   

def gameOver(lives, alphabet):
    if lives == 0:
        print("Game Over you have run out of lives")
        print("The word was", word)
    elif "_" not in wordList:
        print("Congratulations you have won")
        print("The word was", word)
    else:
        guess(lives, alphabet)

word = pick_random_word("words.txt")
wordList = []
for x in word:
    wordList.append("_")

mainmenu()