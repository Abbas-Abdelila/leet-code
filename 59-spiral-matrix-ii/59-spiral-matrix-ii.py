class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        top = 0
        right = n-1
        left = 0
        bottom = n-1
        
        num = 1
        
        ans = [[0]*n for _ in range(n)]
        
        while num <= n*n:
            
            # top row
            for c in range(left,right+1):
                ans[top][c] = num
                num += 1
                
            top += 1
            
            # right col
            for r in range(top,bottom+1):
                ans[r][right] = num
                num += 1
                
            right -= 1
            
            # bottom row
            for c in reversed(range(left,right+1)):
                ans[bottom][c] = num
                num += 1
                
            bottom -= 1
            
            # left col
            for r in reversed(range(top, bottom+1)):
                ans[r][left] = num
                num += 1
                
            left += 1
            
        return ans
        