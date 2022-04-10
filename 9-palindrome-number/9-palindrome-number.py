class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        l = 0
        r = len(s) - 1
        isPalindrome = True
        while l < r:
            if s[l] != s[r]:
                isPalindrome = False
                break
            l += 1
            r -= 1
        return isPalindrome
        
            
            
                
        