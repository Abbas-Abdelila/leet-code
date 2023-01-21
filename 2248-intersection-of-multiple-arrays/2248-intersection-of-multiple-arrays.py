class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common = set(nums[0])
        for arr in nums:
            common = common & set(arr)
        
        if len(common) == 0:
            return []
        
        return sorted(common)
        