class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(target in nums):
            return nums.index(target)
        
        i = 0
        while(i<len(nums) and target > nums[i]):
            i += 1
        
        if(i+1 == len(nums) and nums[len(nums)-1] < target):
            return len(nums)
        return i