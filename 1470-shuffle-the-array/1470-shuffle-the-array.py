class Solution:
    def shuffle(self, nums: List[int], N: int) -> List[int]:
        first = nums[:N]
        second = nums[N:]
        
        ans = []
        for i in range(N):
            ans.append(first[i])
            ans.append(second[i])
        
        return ans
        
        