class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums)+1)
        
        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        remainder_count = {}
        count = 0
        for i in range(len(prefix_sum)):
            remainder = prefix_sum[i] % k
            
            if remainder in remainder_count:
                count += remainder_count[remainder]
            
            if remainder not in remainder_count:
                remainder_count[remainder] = 1
            else:
                remainder_count[remainder] += 1
        
        return count
        
        