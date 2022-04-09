class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if(num in frequency):
                frequency[num] += 1
            else:
                frequency[num] = 1
           
        sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        
        list = []
        
        for i in range(k):
            list.append(sorted_freq[i][0])
        
        return list
            
            
        