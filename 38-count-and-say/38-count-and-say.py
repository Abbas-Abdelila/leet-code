class Solution:
    def countAndSay(self, n: int) -> str:
        
        def map_frequency(numbers):
            res = ""
            count = 1
            ch = numbers[0]
            for i in range(1, len(numbers)):
                if ch == numbers[i]:
                    count += 1
                else:
                    res += str(count) + numbers[i-1]
                    count = 1
                    ch = numbers[i]
                    
            
            res += str(count) + numbers[-1]
            
            return res
        
        start = "1"
        for _ in range(n-1):
            start = map_frequency(start)
            
        
        return start
        
            