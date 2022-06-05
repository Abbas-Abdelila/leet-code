class Solution:
    def totalNQueens(self, N: int) -> int:
        cols = set()
        posDiag = set()
        negDiag = set()
        
        def dfsBacktrack(row):
            if row == N:
                return 1
            
            totalWays = 0
            for c in range(N):
                d1 = row + c
                d2 = row - c
                if c not in cols and d1 not in posDiag and d2 not in negDiag:
                    cols.add(c)
                    posDiag.add(d1)
                    negDiag.add(d2)
                    
                    totalWays += dfsBacktrack(row + 1)
                    
                    negDiag.discard(d2)
                    posDiag.discard(d1)
                    cols.discard(c)
            return totalWays
        
        ans = dfsBacktrack(0)
        return ans