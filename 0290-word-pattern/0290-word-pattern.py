class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # return false if lenght of pattern and words do not match
        
        #use dict to save each element as we go
        #if an element in dict with different value upcoming not matching return false
        
        #if it passes all the iteration return true
        
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        d = {}
        
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = words[i]
            
            if pattern[i] in d:
                if d[pattern[i]] != words[i]:
                    return False
                
        # "abba"
        # "dog dog dog dog" 
        
        # To avoid returning true in the above condition
        unique_keys = set(d.keys())
        unique_vals = set(d.values())
        if len(unique_keys) != len(unique_vals):
            return False 
        
        else:
            return True
        
        