class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        
        # for k > 1 -> sort string
        # for k <= 1 -> Rotate String        
        
        if k > 1:
            return "".join(sorted(s))
        else:
            return min(s[i:]+s[:i] for i in range(len(s)))
            
            