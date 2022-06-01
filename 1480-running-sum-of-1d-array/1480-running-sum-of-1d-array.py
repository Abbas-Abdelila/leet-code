class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        running_sum = [0] * N 
        
        if nums is None:
            return None
        
        for i in range(N):
            for k in range(i+1):
                running_sum[i] += nums[k]
            
        
        return running_sum