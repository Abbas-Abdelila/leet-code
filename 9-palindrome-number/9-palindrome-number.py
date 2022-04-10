class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        left = 0
        right = len(s)-1
        isPalindrome=True
        
        while(left<right):
            if(s[left]!=s[right]):
                isPalindrome=False
                break
            left += 1
            right -= 1
        
        return isPalindrome