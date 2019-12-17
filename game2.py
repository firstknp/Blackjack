class ColorLine:
    def __init__(self, borad ,player ,col):
        self.player = player
        self.board = board
        self.col  = col
    def check_player(self):
        if self.player == "Player2":
            self.play = "Y"
        else:
            self.play = "R"
        return self.play
    def add_chip(self):
        Column = self.col-1
        if self.board[4][Column] == '-':
            self.board[4].pop(Column)
            self.board[4].insert(Column, self.play)
            self.atRow = 1

        elif self.board[3][Column] == '-':
            self.board[3].pop(Column)
            self.board[3].insert(Column, self.play)
            self.atRow = 2

        elif self.board[2][Column] == '-':
            self.board[2].pop(Column)
            self.board[2].insert(Column, self.play)
            self.atRow = 3

        elif self.board[1][Column] == '-':
            self.board[1].pop(Column)
            self.board[1].insert(Column, self.play)
            self.atRow = 4

        elif self.board[0][Column] == '-':
            self.board[0].pop(Column)
            self.board[0].insert(Column, self.play)
            self.atRow = 5

        return self.board
    def check_win(self):
        for x in range(0,-2,-1):
            for i in range(3):
                if self.board[x+4][i] == self.play and self.board[x+4][i+1] == self.play and self.board[x+4][i+2] == self.play and self.board[x+4][i+3] == self.play:
                    return True
                elif self.board[x+4][i] == self.play and self.board[x+3][i] == self.play and self.board[x+2][i] == self.play and self.board[x+1][i] == self.play:
                    return True
                elif self.board[x+4][i] == self.play and self.board[x+3][i+1] == self.play and self.board[x+2][i+2] == self.play and self.board[x+1][i+3] == self.play:
                    return True
                elif self.board[x+4][i+3] == self.play and self.board[x+3][i+3] == self.play and self.board[x+2][i+3] == self.play and self.board[x+1][i+3] == self.play:
                    return True
                elif self.board[x+4][i+3] == self.play and self.board[x+1][i] == self.play and self.board[x+2][i+1] == self.play and self.board[x+3][i+2] == self.play:
                    return True
                elif self.board[x+1][i] == self.play and self.board[x+1][i+1] == self.play and self.board[x+1][i+2] == self.play and self.board[x+1][i+3] == self.play:
                    return True
                elif self.board[x+1][i] == self.play and self.board[x+2][i] == self.play and self.board[x+3][i] == self.play and self.board[x+4][i] == self.play:
                    return True
                elif self.board[x+1][i] == self.play and self.board[x+2][i+1] == self.play and self.board[x+3][i+2] == self.play and self.board[x+4][i+3] == self.play:
                    return True
                elif self.board[x+1][i+3] == self.play and self.board[x+2][i+3] == self.play and self.board[x+3][i+3] == self.play and self.board[x+4][i] == self.play:
                    return True
                elif self.board[x+1][i+3] == self.play and self.board[x+4][i] == self.play and self.board[x+3][i+1] == self.play and self.board[x+2][i+2] == self.play:
                    return True
        for i in range(3):
            if self.board[2][i] == self.play and self.board[2][i+1] == self.play and self.board[2][i+2] == self.play and self.board[2][i+3] == self.play:
                return True

    def check_tie(self):
        if self.board[0][0] != "-" and self.board[0][1] != "-" and self.board[0][2] != "-" and self.board[0][3] != "-" and self.board[0][4] != "-" and self.board[0][5] != "-":
            return True
        


board = [
['-', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-'], 
['-', '-', '-', '-', '-', '-']]
def Borad(board):
    for r in range(len(board)):
        print("")
        print(board[r])
    print("------------------------------")
    print("  1    2    3    4    5    6")
    print("------------------------------")


def start_colorLine(user):
    print("Wellcome to ColorLine")
    print("-----------Let Start-----------")
    player = 1
    while True:
        Borad(board)
        if player % 2 == 0:
            play = "Player2"
            color = "Yellow"
        elif player % 2 != 0:
            play = user
            color = "RED"
        print("Please select column")
        print("========")
        print(f"{play} ({color})")
        print("========")
        num_col = input("Enter number 1 - 6: ")
        if num_col in ["1","2","3","4","5","6"]:
            a = ColorLine(board, play ,int(num_col))
            a.check_player()
            a.add_chip()
            a.check_win()
            a.check_tie()
            if a.check_win() == True:
                Borad(board)
                if play == "Player1":
                    print(f"{play} Win (RED)")
                else:
                    print("Player2 Win (YELLOW)")

                print("Thankyou for playing")
                break
            if a.check_tie() == True:
                Borad(board)
                print("Tie")
                print("Thankyou for playing")
                break
            player += 1
        else:
            print("Error input")
            print("Please enter number again")
            pass

if __name__ == "__main__":
    start_colorLine("user")