import symbols
import minmax
import tictactoe

if __name__ == '__main__':

    print("Welcome to the Tic Tac Toe Game!")
    print("1:playing against computer")
    print("2:playing against another player")
    while True:
        try:
            option = int(input("choose one of the options:"))
        except:
            print("The input must be a number !!!")
            continue

        if not (option == 1 or option == 2):
            print("The number must be 1 or 2 !!!")
        else:
            break
    
    
    if option == 1:
        print("starting with:")
        print("1:X")
        print("2:O")

        while True:
            try:
                start_with = int(input("choose one of the options:"))
            except:
                print("The input must be a number !!!")
                continue
            
            if not (start_with == 1 or start_with == 2):
                print("The number must be 1 or 2 !!!")
            else:
                break
        



    table = [[1,2,3],
            [4,5,6],
            [7,8,9]]

    tictactoe.showTable(table)

    print("Game just started ....")

    
    if option == 1:
        if start_with == 1:
            cpt = 1
            while(not tictactoe.winCheck(table) and tictactoe.endCheck(table)):
                cpt += 1
                if cpt % 2 == 0:
                    try:
                        nb = int(input("Player , please select a number:"))
                    except :
                        print("The input must be a number !!!")
                        cpt-=1
                        continue
                    index = tictactoe.chooseCase(nb)
                    if index == (-1,-1):
                        print("The number must be between 1 and 9!!!")
                        cpt-=1
                        continue
                    if table[index[0]][index[1]] == 'O' or table[index[0]][index[1]] == 'X':
                        print("The box is already filled!!!")
                        cpt-=1
                        continue
                    table[index[0]][index[1]] = symbols.symbol[0]
                else:
                    print("Computer playing !!!")
                    index=minmax.findBestMoveForO(table)
                    table[index[0]][index[1]] = symbols.symbol[1] 
                tictactoe.showTable(table)

            if tictactoe.winCheck(table) == 10:
                print("The winner is the player !")

            if tictactoe.winCheck(table) == -10:
                print("The winner is the robot !")

        else:
            cpt = 0
            while(not tictactoe.winCheck(table) and tictactoe.endCheck(table)):
                cpt+=1
                if cpt % 2 == 0:
                    try:
                        nb = int(input("Player , please select a number:"))
                    except :
                        print("The input must be a number !!!")
                        cpt-=1
                        continue
                    index = tictactoe.chooseCase(nb)
                    if index == (-1,-1):
                        print("The number must be between 1 and 9!!!")
                        cpt-=1
                        continue
                    if table[index[0]][index[1]] == 'O' or table[index[0]][index[1]] == 'X':
                        print("The box is already filled!!!")
                        cpt-=1
                        continue
                    table[index[0]][index[1]] = symbols.symbol[1]
                else:
                    print("Computer playing !!!")
                    index=minmax.findBestMoveForX(table)
                    table[index[0]][index[1]] = symbols.symbol[0] 
                tictactoe.showTable(table)

            if tictactoe.winCheck(table) == 10:
                print("The winner is the robot !")

            if tictactoe.winCheck(table) == -10:
                print("The winner is the Player !")   
    else:
        cpt = 1
        while(not tictactoe.winCheck(table) and tictactoe.endCheck(table)):
            cpt += 1
            try:
                nb = int(input("Player " + str((cpt % 2)+1) +", please select a number:"))
            except :
                print("The input must be a number !!!")
                cpt-=1
                continue
            index = tictactoe.chooseCase(nb)
            if index == (-1,-1):
                print("The number must be between 1 and 9!!!")
                cpt-=1
                continue
            if table[index[0]][index[1]] == 'O' or table[index[0]][index[1]] == 'X':
                print("The box is already filled!!!")
                cpt-=1
                continue
            if cpt % 2 == 0:
                table[index[0]][index[1]] = symbols.symbol[0]
            else:
                table[index[0]][index[1]] = symbols.symbol[1]

            tictactoe.showTable(table)
        
        if tictactoe.winCheck(table) == 10:
            print("The winner is Player 1 !")

        if tictactoe.winCheck(table) == -10:
            print("The winner is Player 2 !")
            

    if not tictactoe.endCheck(table):
        print("Game over!  No one wins!")
