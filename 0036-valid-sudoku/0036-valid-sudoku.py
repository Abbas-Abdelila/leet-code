class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (self.is_row_valid(board) and 
               self.is_col_valid(board) and 
               self.is_square_board_valid(board))
        
    def is_row_valid(self,board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True               

            
        # Make sure it is valid sudoku across column
    def is_col_valid(self,board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True

        # Make sure the 3x3 board elements have no repeated digit 1-9
    def is_square_board_valid(self,board):
        for i in (0,3,6):
            for j in (0,3,6):
                square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_unit_valid(square):
                    return False

        return True
        
        # Unit validate
    def is_unit_valid(self, unit):
        ans = [i for i in unit if i!="."]
        return len(ans) == len(set(ans))

        
        