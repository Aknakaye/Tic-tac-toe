def showTable(table):
    print("\n")
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j], end="  ")
        print("\n")


def chooseCase(nb):
    if nb == 1 :
        i = 0 
        j= 0 
    elif nb == 2 :
        i = 0 
        j= 1
    elif nb == 3:
        i = 0 
        j= 2
    elif nb == 4:
        i = 1 
        j= 0
    elif nb == 5:
        i = 1 
        j= 1
    elif nb == 6:
        i = 1 
        j= 2
    elif nb == 7:
        i = 2 
        j= 0
    elif nb == 8:
        i = 2 
        j= 1
    elif nb == 9:
        i = 2 
        j= 2
    else:
        i=-1
        j=-1

    return (i,j)
        

def winCheck(board) :
    for i in range(len(board)) :
        if board[i][0] != 'X' and board[i][0] == board[i][1] and board[i][1] == board[i][2]: 
            return -10

        if  board[i][0] != 'O' and board[i][0] == board[i][1] and board[i][1] == board[i][2]: 
            return 10
        
        if board[0][i] != 'X' and board[0][i] == board[1][i] and board[1][i] == board[2][i]: 
            return -10

        if  board[0][i] != 'O' and board[0][i] == board[1][i] and board[1][i] == board[2][i]: 
            return 10
        
    if board[1][1] != 'X' and board[0][0] == board[1][1] and board[1][1] == board[2][2]: 
            return -10

    if  board[1][1] != 'O' and board[0][0] == board[1][1] and board[1][1] == board[2][2]: 
            return 10

    if board[1][1] != 'X'  and board[0][2] == board[1][1] and board[1][1] == board[2][0]: 
            return -10

    if board[1][1] != 'O' and board[0][2] == board[1][1] and board[1][1] == board[2][0]: 
            return 10
     
    return 0
            

def endCheck(table):
    cpt=0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 'O' or table[i][j] == 'X':
                cpt +=1
    if cpt == 9:
        return 0
    else:
        return 1