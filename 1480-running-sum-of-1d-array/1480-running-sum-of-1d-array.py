class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        running_sum = [nums[0]] * N
        
        if nums is None:
            return None
        
        for i in range(1,N):
            running_sum[i] = running_sum[i-1] + nums[i]
        
        return running_sum
        
        