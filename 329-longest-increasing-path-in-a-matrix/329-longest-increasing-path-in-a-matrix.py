class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        R = len(matrix)
        C = len(matrix[0])
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        has_cache = [[False] * C for _ in range(R)]
        cache = [[None] * C for _ in range(R)]
        
        
        
        def longest(x,y):
            best = 1
            
          
            
            if has_cache[x][y]:
                return cache[x][y]
            
            for dx,dy in directions:
                nx,ny = x+dx, y+dy
            
                if 0 <= nx < R and 0 <= ny <C and matrix[x][y] < matrix[nx][ny]:
                    best = max(best, longest(nx,ny)+1)
                
            has_cache[x][y] = True
            cache[x][y] = best
            
            return best
        
        
        best = 0
        for x in range(R):
            for y in range(C):
                best = max(longest(x,y), best)
        
        return best
        
                
        
        
        