class Solution:
    def reverseWords(self, s: str) -> str:
        strings = s.split(" ")
        for idx, string in enumerate(strings):
            strings[idx] = string[::-1]
        
        return " ".join(strings)
        