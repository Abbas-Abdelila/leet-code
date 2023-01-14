class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d = {i:i for i in string.ascii_lowercase}
        
        def find(x):
            if d[x] != x:
                d[x] = find(d[x])
            return d[x]
        
        def union(x, y):
            rx, ry = find(x), find(y)
            if d[rx] < d[ry]:
                d[ry] = rx
            else:
                d[rx] = ry
        
        for a, b in zip(s1, s2):
            union(a, b)
			
        # step3
        ans = ''
        for s in baseStr:
            ans += find(s)
        return ans