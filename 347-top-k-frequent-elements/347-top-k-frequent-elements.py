class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if(num in frequency):
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        result = []
        for key,value in frequency.items():
            result.append([key,value])
            
        result.sort(key=lambda x:x[1], reverse=True)
        
        return [x[0] for x in result[:k]]
           
       
            
        