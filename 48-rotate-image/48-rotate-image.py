class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # reverse it and transpose it
        N = len(matrix)
        
        
        matrix.reverse()
        
        for i in range(N):
            for j in range(i): # the lower triangle since we are swapping both
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
        
        

        
        
        