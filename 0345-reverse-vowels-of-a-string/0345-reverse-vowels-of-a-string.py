class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list('aeouiAEOUI')

        l, r = 0, len(s)-1
        string = list(s)

        while l < r:
            if string[l] in vowels and string[r] in vowels:
                string[l], string[r] = string[r], string[l]
                l += 1
                r -= 1
            if string[l] not in vowels:
                l += 1
            if string[r] not in vowels:
                r -= 1
            
        return "".join(string)