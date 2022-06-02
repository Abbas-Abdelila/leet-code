class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        R = len(matrix)
        C = len(matrix[0])
        
        transpose = [[ [None] for _ in range(R)] for _ in range(C)]
        
        for i in range(C):
            for j in range(R):
                transpose[i][j] = matrix[j][i]
                
        return transpose
