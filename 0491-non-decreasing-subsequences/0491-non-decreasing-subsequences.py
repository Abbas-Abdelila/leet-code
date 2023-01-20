class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        ans = set()
        def BT(i, subsequence):
            nonlocal ans
            
            if len(subsequence) > 1:
                ans.add(tuple(subsequence))
            
            if i == len(nums):
                return 
            
            #Two cases wether to take it or not
            if not subsequence or  nums[i] >= subsequence[-1]:
                BT(i+1, subsequence+[nums[i]])
                
            # or skip it    
            BT(i+1, subsequence)
        
        BT(0, [])
        
        return ans