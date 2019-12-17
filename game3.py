import random

class Hangman:
    attempts = 0
    total_attempts = 6
    def __init__(self, word):
        self.word = word
        self.file = open("words.txt", "r")
        for line in self.file:
            self.wordlist = line.split()
    def randomworld(self, wordlist):
        return random.choice(self.wordlist)
    # def playapp(self):

def drawhangman(guesses):
    if (guesses==0):
        print ("_________")
        print ("|	 |")
        print ("|")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
    elif (guesses==1):
        print ("_________")
        print ("|	 |")
        print ("|    O")
        print ("|")
        print ("|")
        print ("|")
        print ("|________")
    elif (guesses==2):
        print ("_________")
        print ("|	 |")
        print ("|    O")
        print ("|    |")
        print ("|    |")
        print ("|")
        print ("|________")
    elif (guesses==3):
        print ("_________")
        print ("|	 |")
        print ("|    O")
        print ("|   \|")
        print ("|    |")
        print ("|")
        print ("|________")
    elif (guesses==4):
        print ("_________")
        print ("|	 |")
        print ("|    O")
        print ("|   \|/")
        print ("|    |")
        print ("|")
        print ("|________")
    elif (guesses==5):
        print ("_________")
        print ("|	 |")
        print ("|    O")
        print ("|   \|/")
        print ("|    |")
        print ("|   /")
        print ("|________")
    elif (guesses==6):
        print ("_________")
        print ("|	 |")
        print ("|    O")
        print ("|   \|/")
        print ("|    |")
        print ("|   /|\")
        print ("|________")
        print("")
        