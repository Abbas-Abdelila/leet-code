class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            remaining = target - val
            
            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[val] = i