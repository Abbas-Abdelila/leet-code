class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        lookup = {}
        # Create the dictionary
        for idx, ch in enumerate(order):
            lookup[ch] = idx+1
            
        size = len(words) - 1
        
        for i in range(size):
            w = min(len(words[i]), len(words[i+1]))
            
            for j in range(w):
                if lookup[words[i][j]] < lookup[words[i+1][j]]:
                    break
                elif lookup[words[i][j]] == lookup[words[i+1][j]]:
                    continue
                
                else:
                    return False
            if words[i][:w] == words[i+1][:w] and len(words[i]) > len(words[i+1]):
                return False
                
            
        return True
            