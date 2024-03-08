class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        freq_max = max(freq.values())
        
        result = 0
        for k, v in freq.items():
            if v == freq_max:
                result += freq_max
        
        return result