class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        
        count_s1 = [0] * 26
        count_s2 = [0] * 26
        
        if (n1 > n2):
            return False
        
        # Populate with size of s1 both counters
        for i in range(n1):
            count_s1[ord(s1[i]) - ord("a")] += 1
            count_s2[ord(s2[i]) - ord("a")] += 1
            
        for i in range(n1,n2):
            if count_s1 == count_s2:
                return True
            
            count_s2[ord(s2[i]) - ord('a')] += 1
            count_s2[ord(s2[i-n1]) - ord('a')] -= 1
        
        return count_s1 == count_s2