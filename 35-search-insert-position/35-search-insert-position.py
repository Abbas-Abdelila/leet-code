class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)
        
        while(l < r):
            mid = (l + r) // 2
            
            if (target <= nums[mid]):
                r = mid
            else:
                l = mid + 1
        
        return l