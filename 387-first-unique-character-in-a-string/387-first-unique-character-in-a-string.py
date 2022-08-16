class Solution(object):
    def firstUniqChar(self, s):
        freq = collections.Counter(s)
        
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
            
        return -1
