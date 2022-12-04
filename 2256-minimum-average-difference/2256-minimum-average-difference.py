class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:

        n = len(nums) 
        
        pref = list(accumulate(nums))
        
        ans = (pref[-1]//n, n-1)     
  
        for i in range(n-1):         
            diff = abs(pref[i]//(i+1) - (pref[-1] - pref[i])//(n-i-1))    
            ans  = min(ans, (diff,i))                   
        return ans[1]                                   