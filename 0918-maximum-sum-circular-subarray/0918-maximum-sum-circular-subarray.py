class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        k = self.kadane(nums)
        
        cirSum = 0
        
        for idx in range(len(nums)):
            cirSum += nums[idx]
            nums[idx] = nums[idx] * (-1)
        
        cirSum = cirSum + self.kadane(nums)
        
        if cirSum > k and cirSum != 0:
            return cirSum
        else:
            return k
        
        
    def kadane(self, nums_list):
            Sum, maxSum = nums_list[0], nums_list[0]
            
            for m in nums_list[1:]:
                Sum = max(m, Sum + m)
                maxSum = max(Sum, maxSum)
            
            return maxSum
        
        
        
            