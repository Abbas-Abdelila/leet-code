class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        col_size = len(mat[0])-1
        
        for i in range(len(mat)):
            total += mat[i][i]
            
            if i != col_size - i:
                total += mat[i][col_size-i]
        
        return total
        