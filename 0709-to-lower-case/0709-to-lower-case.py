class Solution:
    def toLowerCase(self, s: str) -> str:
        asci = []
        for ch in s:
            if ord(ch) <= 90 and ord(ch) >= 65:
                asci.append(chr(ord(ch) + 32))
            else:
                asci.append(ch)
        
        return "".join(asci)