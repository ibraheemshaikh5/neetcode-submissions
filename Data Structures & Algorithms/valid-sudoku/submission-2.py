class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check downwards
        for c in range(9):
            uniques = set()
            for r in range(9):
                if board[r][c] != '.': 
                    if board[r][c] in uniques:
                        return False
                    else:
                        uniques.add(board[r][c])

        # check across
        for r in range(9):
            uniques = set()
            for c in range(9):
                if board[r][c] != '.': 
                    if board[r][c] in uniques:
                        return False
                    else:
                        uniques.add(board[r][c])

        # grid iteration
        row_max = 3 
        col_max = 3
        while row_max <= 9 and col_max <= 9:
            uniques = set()
            for c in range(col_max - 3, col_max):
                for r in range(row_max - 3, row_max):
                    if board[r][c] != '.':
                        if board[r][c] in uniques:
                            return False
                        else:
                            uniques.add(board[r][c])
            
            if (row_max != 9):
                row_max += 3
            else:
                row_max = 3
                col_max += 3

        return True