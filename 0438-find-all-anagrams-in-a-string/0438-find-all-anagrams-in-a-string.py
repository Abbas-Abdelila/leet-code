class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        n1, n2 = len(s), len(p)
        if n2 > n1:
            return ans
        
        count_s = [0] * 26
        count_p = [0] * 26
        
        for i in range(n2):
            count_s[ord(s[i]) - ord('a')] += 1
            count_p[ord(p[i]) - ord('a')] += 1
            
             
        for i in range(n2, n1):
            if count_s == count_p:
                ans.append(i-n2)
            
            count_s[ord(s[i]) - ord('a')] += 1
            count_s[ord(s[i-n2]) - ord('a')] -= 1
        
        if count_s == count_p:
            ans.append(len(s)-len(p))
        
        return ans
