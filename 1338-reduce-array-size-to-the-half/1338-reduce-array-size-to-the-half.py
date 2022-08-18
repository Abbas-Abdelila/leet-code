class Solution(object):
    def minSetSize(self, arr):
        N = len(arr)
        freq = collections.Counter(arr)
        total = N
        
        sorted_arr = sorted(freq.values(), reverse=True) 
        # Another way to reverse it is
        # sorted(freq.values(), key=lambda x: -x) b|c it sorts the negative form 
        for i, val in enumerate(sorted_arr):
            total -= val
            if(total * 2 <= N):
                return i+1
            
    
        
        
        
        