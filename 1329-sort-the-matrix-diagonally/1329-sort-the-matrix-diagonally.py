class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        R = len(mat)
        C = len(mat[0])
        
        diagonals = defaultdict(list)
        for i in range(R):
            for j in range(C):
                k = i-j
                diagonals[k].append(mat[i][j])
        
        for k in diagonals:
            diagonals[k] = sorted(diagonals[k], reverse=True)
        
        for i in range(R):
            for j in range(C):
                k = i-j
                mat[i][j] = diagonals[k].pop()
        
        return mat
        
        
            
        