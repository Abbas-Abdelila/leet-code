class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        counter = [0,0,0]
        for num in nums:
            counter[num] += 1
        
        cumulative = []
        total = 0
        for count in counter:
            total += count
            cumulative.append(total)
        
        output = [0]*N
        for i in range(N-1, -1, -1):
            cumulative[nums[i]] -= 1
            output[cumulative[nums[i]]] = nums[i]
        
        for i in range(N):
            nums[i] = output[i]
            
