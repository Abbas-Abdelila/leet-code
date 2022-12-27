class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        diff = sorted(c - r for c, r in zip(capacity, rocks))
        i = 0
        count = 0
        
        while i < len(diff) and additionalRocks >= diff[i]:
            additionalRocks -= diff[i]
            count += 1
            i += 1
        
        return count