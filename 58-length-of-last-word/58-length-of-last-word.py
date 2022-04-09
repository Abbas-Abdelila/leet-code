class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split(' ') #strip gets rid of whitespace on the left and right
        return len(words[len(words)-1])
        