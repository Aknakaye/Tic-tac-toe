import re 
import symbols 
import tictactoe


def minimax(board,isMax) :
    score = tictactoe.winCheck(board)

    if score == 10 or score == -10 :
        return score

    if tictactoe.endCheck(board) == 0 :
        return 0

    if (isMax) :    
        best = -1000

        for i in range(3) :        
            for j in range(3) :
                if re.search('[1-9]' , str(board[i][j])):
                    temp = board[i][j]
                    board[i][j] = symbols.symbol[0]
                    bestScore = minimax(board,False)
                    board[i][j] = temp
                    best = max( bestScore,best)

                    
        return best

    else :
        best = 1000

        for i in range(3) :        
            for j in range(3) :

                if re.search('[1-9]' , str(board[i][j])):
                    temp = board[i][j]
                    board[i][j] = symbols.symbol[1]

                    bestScore = minimax(board,True)
                    board[i][j] = temp
                    best = min(bestScore,best)
        return best




def findBestMoveForO(board) :
    bestVal = 1000
    bestMove = (-1, -1)

    for i in range(3) :    
        for j in range(3) :

            if re.search('[1-9]' , str(board[i][j])) :
                temp = board[i][j]
                board[i][j] = symbols.symbol[1]

                moveVal = minimax(board,True)

                board[i][j] = temp

                if (moveVal < bestVal) :     
                    bestVal = moveVal
                    bestMove = (i, j)

    return bestMove

    

def findBestMoveForX(board) :
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3) :    
        for j in range(3) :

            if re.search('[1-9]' , str(board[i][j])) :
                temp = board[i][j]
                board[i][j] = symbols.symbol[0]

                moveVal = minimax(board,False)

                board[i][j] = temp

                if (moveVal > bestVal) :     
                    bestVal = moveVal
                    bestMove = (i, j)

    return bestMove