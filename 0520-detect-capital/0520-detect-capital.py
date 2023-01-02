class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Use the count of capitals
        num_of_capital = 0
        N = len(word)
        
        for ch in word:
            num_of_capital += ch.isupper()
            
        return ((num_of_capital == N) or 
               (num_of_capital == 1 and word[0].isupper()) or 
               (num_of_capital == 0))
            