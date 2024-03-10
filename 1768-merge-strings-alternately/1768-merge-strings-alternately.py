class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word1_length = len(word1)
        word2_length = len(word2)
        merged = ""
        
        for i in range(min(word1_length, word2_length)):
            merged += word1[i] + word2[i]
            
        if word1_length > word2_length:
            merged += word1[word2_length:]
        
        if word1_length < word2_length:
            merged += word2[word1_length:]
        
        return merged