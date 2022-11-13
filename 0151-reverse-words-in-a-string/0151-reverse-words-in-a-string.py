class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.strip().split(' ')
        while '' in string:
            string.remove('')
                
        return " ".join(reversed(string))