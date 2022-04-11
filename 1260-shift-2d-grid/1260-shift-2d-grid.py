class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        R = len(grid)
        C = len(grid[0])
        
        matrix = [[None]*C for _ in range(R)]
        
        def shift(x,y,k):
            position = (x*C + y + k) % (R*C) # to keep it in range
            
            return (position // C, position % C)
        
        for i in range(R):
            for j in range(C):
                pi, pj = shift(i,j,k)
                matrix[pi][pj] = grid[i][j]
                
        
        return matrix
        