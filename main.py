import sys
menu = input("Enter your status (admin/player): ")
while True:
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
                break