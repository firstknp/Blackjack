from game1 import *
from game2 import *
from game3 import *

import sys
userlist = []
# class GameStat:
#     def __init__(self,game ,win, user_num , userlist):
#         self.game = game
#         self.win = win
#         self.user_num = user_num
#         self.userlist = userlist
#     def check_game(self):
#         if self.game == "blackjack":
#             if self.win == "win":
#                 self.userlist[self.user_num][1][1] += 1
#         elif self.game == "hangman":
#             if self.win == "win":
#                 self.userlist[self.user_num][1][1] += 1
        
class Player:
    def __init__(self, user, userlist):
        self.user = user
        self.userlist = userlist
    def check_user(self):
        for i in range(len(userlist)):
            if self.user == self.userlist[i][0]:
                return i

class PlayerHandler:
    def __init__(self,user,list1):
        self.user = user
        self.list1 = list1

    def add_user(self):
        self.list1.append([ self.user,[0,0],[0,0],[0,0],1000 ])

    def show_user(self):
        print(f"{self}")




while True:
    menu = input("Enter your status (admin/player): ")
    if menu == 'admin':
        while True:
            print("")
            print("Select your choice")
            choice = int(input("1. Add new player \n2. Show players \n3. Add player's balance \n4. Quit \n"))
            if choice == 1:
                name = input("Enter player's name: ")
                play = PlayerHandler(name, userlist)
                play.add_user()
            elif choice == 2:
                for i in range(len(userlist)):
                    print(f"{userlist[i][0]}: Balance = {userlist[i][4]}")
                    print(f"Blackjack: #plays = {userlist[i][1][0]} #wins = {userlist[i][1][1]}")
                    print(f"ColorLine: #plays = {userlist[i][2][0]} #wins = {userlist[i][2][1]}")
                    print(f"Hangman: #plays = {userlist[i][3][0]} #wins = {userlist[i][3][1]}")
            elif choice == 3:
                name = input("Enter player's name: ")
                for i in range(len(userlist)):
                    if name == userlist[i][0]:
                        bal = int(input("Enter player's added balance: "))
                        userlist[i][4] += bal

            if choice == 4:
                back = input("Back to Main ot Quit(M/Q): ")
                if back == 'M':
                    break
                elif back == 'Q':
                    sys.exit
                
    elif menu == 'player':
        name = input("Enter your name: ")
        play = PlayerHandler(name, userlist)
        play.add_user()
        while True:
            print("")
            print("Select your choice")
            selection = int(input("1. Play Blackjack \n2. Play Colorline \n3. Play Hangman \n4. See your profile \n5. Stop playing\n"))
            print (f"Welcome {name}")
            if selection == 1:         
                game = Rungame()
                game.play()
                for i in range(len(userlist)):
                    userlist[i][4] -= 20
                # if game.get_win_game1() == "win":
                #     a = Player(name,userlist)
                #     GameStat("blackjack","win",a.check_user ,userlist)
            elif selection == 2:
                start_colorLine(name)
                for i in range(len(userlist)):
                    userlist[i][4] -= 10
                # game = ColorLine(board, play ,int(num_col))
                # if game.get_win_game2() == "win":
                #     GameStat("blackjack","win")
            elif selection == 3:
                game = Game()
                game.play()
                for i in range(len(userlist)):
                    userlist[i][4] -= 15
                # if game.get_win_game3() == "win":
                #     a = Player(name,userlist)
                #     GameStat("hangman","win",a.check_user ,userlist)
            elif selection == 4:
                for i in range(len(userlist)):
                    print(f"{userlist[i][0]}: Balance = {userlist[i][4]}")
            elif selection == 5:
                break
        main = input("Back to Main or Quit (M/Q): ")
        if main == "Q":
            break

        
f = open('player.txt', 'r')



