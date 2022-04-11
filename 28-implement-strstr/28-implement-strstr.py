class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # sliding window
        
        if(needle==""):
            return 0
        
        left = 0
        window_size = len(needle)
        
        while(left+window_size <= len(haystack)):
            if(haystack[left:left+window_size] == needle):
                return left
            
            left += 1
        
        return -1