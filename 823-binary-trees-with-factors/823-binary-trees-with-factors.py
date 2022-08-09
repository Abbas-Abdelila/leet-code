class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        
        allowed = set(arr)
        
        cache = {}
        
        def go(node):
            total = 1
            if node in cache:
                return cache[node]
            
            for x in arr:
                if node%x == 0 and node//x in allowed:
                    total += go(x) * go(node//x)
                    total %= MOD
                    
            cache[node] = total
            return total
        
        total = 0
        
        for x in arr:
            total += go(x)
            total %= MOD
        
        return total