class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        ans = []
        n = [a for a in changed if a < 0]
        p = [a for a in changed if a >= 0]
        arr = sorted(n, reverse=True) + sorted(p)
        c = Counter(arr)
        if len(arr)%2 != 0:
            return []
        for a in arr:
            if c[a] == 0:
                ans.append(a//2)
                continue
            
            if c[2*a] == 0: return []
            c[a] -= 1
            c[2*a] -= 1

        
        return ans
              
        