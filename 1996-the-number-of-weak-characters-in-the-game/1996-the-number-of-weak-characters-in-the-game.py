class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1])) #attack(DESC) and defence(ASCE)
        limit = float(-inf)
        
        ans = 0
        for attack, defence in properties:
            if defence < limit:
                ans += 1
            limit = max(limit, defence)
            
        return ans