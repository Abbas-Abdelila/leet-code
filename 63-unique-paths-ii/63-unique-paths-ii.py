class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R,C = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0 for _ in range(C)] for _ in range(R)]
        print(dp)
        
        # fill the first row with 1 but if there is 1 already break
        for c in range(C):
            if obstacleGrid[0][c] == 1:
                break
            dp[0][c] = 1
            
        # fill the first column with 1 but if there is 1 already break
        for r in range(R):
            if obstacleGrid[r][0] == 1:
                break
            dp[r][0] = 1
        
        for r in range(1,R):
            for c in range(1,C):
                if obstacleGrid[r][c] == 1:
                    continue
                dp[r][c] = dp[r-1][c]+ dp[r][c-1]
            
        return dp[-1][-1]