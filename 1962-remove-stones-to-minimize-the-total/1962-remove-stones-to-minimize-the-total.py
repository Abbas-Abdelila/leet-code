class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        h = []
        
        for x in piles:
            heapq.heappush(h, -x)
        
        for _ in range(k):
            curr = -heapq.heappop(h)
            curr -= curr // 2
            heapq.heappush(h, -curr)
        
        return -sum(h)