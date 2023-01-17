class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cost = 0
        for x in s:
            if x == "0":
                cost += 1
        
        best = cost
        for x in s:
            if x == "0":
                cost -= 1
            else:
                cost += 1
            best = min(best, cost)
        
        return best