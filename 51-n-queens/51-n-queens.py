class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        
        ans = []
        
        def backtrack(row, board, col_set, diag_set, anti_diag_set):
            if row == n:
                current = []
                for row in board:
                    current.append("".join(row[:]))
                    
                ans.append(current)
                return
            
            for col in range(n):
                if col not in col_set and (row - col) not in diag_set and (row + col) not in anti_diag_set:
                    board[row][col] = "Q"
                    col_set.add(col)
                    diag_set.add(row - col)
                    anti_diag_set.add(row+col)
                    
                    backtrack(row+1, board, col_set, diag_set, anti_diag_set)
                    
                    board[row][col] = "."
                    col_set.discard(col)
                    diag_set.discard(row - col)
                    anti_diag_set.discard(row+col)
                    
        backtrack(0, board, set(), set(), set())
        
        return ans