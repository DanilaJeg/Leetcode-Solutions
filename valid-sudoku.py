class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        for i in range(1, 10):
            cols[i] = set()
            rows[i] = set() 
        # key is gonna be (r / 3, c / 3)
        squares = {}
        for i in range(3):
            for j in range(3):
                squares[(i, j)] = {}
        
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (board[row][col] in cols[col] or board[row][col] in rows[row] or board[row][col] in squares[(row // 3, col // 3)]):
                    return False
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])
        return True
