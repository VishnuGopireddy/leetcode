class Solution:
    def __init__(self):
        self.n = None
        self.sol = []
        self.board = [['.' for i in range(4)] for _ in range(4)]

    def solveNQueens(self, n):
        self.n = n
        self.board = [['.' for i in range(n)] for _ in range(n)]
        self.solnQueen(0)
        return self.sol

    def valid(self, row, col):
        # check two queens in one row
        for i in range(col):
            if self.board[row][i] == 'Q':
                return False

        # check two top left diag
        for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
            if self.board[i][j] == 'Q':
                return False

        for i,j in zip(range(row,self.n), range(col,-1,-1)):
            if self.board[i][j] == 'Q':
                return False

        return True

    def solnQueen(self, col):
        if col == self.n:
            self.sol.append(str(i) for i in self.sol)
            return True

        for i in range(self.n):
            if self.valid(i, col):
                self.board[i][col] = 'Q'
                if self.solnQueen(col+1):
                    return
                else:
                    self.board[i][col] = '.'

if __name__ == '__main__':
    sol = Solution()
    print(sol.solveNQueens(4))