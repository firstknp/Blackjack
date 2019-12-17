from game1 import *
from game2 import *
from game3 import *

import sys

menu = input("Enter your status (admin/player): ")
if menu == 'admin':
    print("")
    print("Select your choice")
    choice = int(input("1. Add new player \n2. Show players \n3. Add player's balance \n4. Quit \n"))
    if choice == 4:
        back = input("Back to Main ot Quit(M/Q): ")
        if back == 'M':
            menu = input("Enter your status (admin/player): ")
        elif back == 'Q':
            sys.exit
            
elif menu == 'player':
    name = input("Enter your name: ")
    while True:
        print("")
        print("Select your choice")
        selection = int(input("1. Play Blackjack \n2. Play Colorline \n3. Play Hangman \n4. See your profile \n5. Stop playing\n"))
        print (f"Welcome {name}")
        if selection == 1:         
            game = Rungame()
            game.play()
        elif selection == 2:
            start_colorLine(name)
        elif selection == 3:
            game = Game()
            game.play()
        elif selection == 5:
            sys.exit

