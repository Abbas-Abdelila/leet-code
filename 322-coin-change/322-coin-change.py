class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        INF = 10 ** 21
        
        has_cache = [False] * (amount+1)
        cache = [None] * (amount+1)
        
        def getMin(amount):
            
            
            
            if amount == 0:
                return 0
            
            if has_cache[amount]:
                return cache[amount]
            
            best = INF
            
            for coin in coins:
                if amount >= coin:
                    best = min(best, getMin(amount-coin)+1)
            
            has_cache[amount] = True
            cache[amount] = best
            return best
        
        ans = getMin(amount)
        if ans >= INF:
            return -1
        return ans
            
            