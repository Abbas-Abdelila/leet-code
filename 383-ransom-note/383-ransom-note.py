class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        chars = [0] * 26
        for ch in magazine:
            chars[ord(ch)-ord('a')] += 1
        
        for ch in ransomNote:
            chars[ord(ch)-ord('a')] -= 1
            
            if chars[ord(ch)-ord('a')] == -1:
                return False
        
        return True
            
        
        
        
        
        