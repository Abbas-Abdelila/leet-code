class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
                
        print(freq)
            
        
        res = []
        
        for key, val in freq.items():
            if val == 1:
                res.append(key)
                
        if not res:
            return -1
        index = s.index(res[0])
        for ch in res:
            if s.index(ch) < index:
                index = s.index(ch)
            
        return index
        