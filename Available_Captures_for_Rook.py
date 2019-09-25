#https://leetcode.com/problems/available-captures-for-rook/

def numRookCaptures(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                row,col = i,j
    pos = row
    print(row,col)
    up = down =left = right = 0
    #Downwards
    while pos < 8:
        if board[pos][col] == 'B':
            break
        elif board[pos][col] == '.':
            pass
        elif board[pos][col] == 'p':
            down = 1
            break
        pos = pos + 1
#    print(down)
#    print('----')
#UPwards
    pos = row
    while pos >= 0:
        if board[pos][col] == 'B':
            break
        elif board[pos][col] == '.':
            pass
        elif board[pos][col] == 'p':
            up = 1
            break
        pos = pos - 1
#    print(up)
#    print('------')

    #RIGHT
    pos = col
    while pos < 8:
        if board[row][pos] == 'B':
            break
        elif board[row][pos] == '.':
            pass
        elif board[row][pos] == 'p':
            right = 1
            break

        pos = pos + 1
#    print(right)
#    print('------')

    #LEFT
    pos = col
    while pos >= 0:
        if board[row][pos] == 'B':
            break
        elif board[row][pos] == '.':
            pass
        elif board[row][pos] == 'p':
            left = 1
            break
        pos = pos - 1
#    print(left)
#    print('------')
    print(up+down+left+right)

board = [[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","R",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
numRookCaptures(board)
