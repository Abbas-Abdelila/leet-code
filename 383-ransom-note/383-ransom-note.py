class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            magazine_dict = collections.Counter(magazine)    
            for ch in ransomNote:
                if ch in magazine and ransomNote.count(ch) <= magazine_dict[ch]:
                    continue
                else: 
                    return False
            
            return True
            