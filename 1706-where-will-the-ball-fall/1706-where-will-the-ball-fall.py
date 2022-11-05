class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        width = len(grid[0])
        
        def column_check(x):
            for h in range(len(grid)):
                if x < width-1 and grid[h][x] + grid[h][x+1] == 2:
                    x += 1
                elif x > 0 and grid[h][x] + grid[h][x-1] == -2:
                    x -= 1
                else:
                    return -1
            
            return x
        
        return [column_check(i) for i in range(width)]