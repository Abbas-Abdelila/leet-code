class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
#  --->Brute Force Method 

#         def isSubsequence(word):
            
#             i = 0
#             for c in s:
#                 if i < len(word) and c == word[i]:
#                     i += 1
                
#                 if i == len(word):
#                     return True
            
#             return False
        
#         ans = 0
#         for w in words:
#             if isSubsequence(w):
#                 ans += 1 
        
#         return ans

# --->> Optimal Approach 

        def isSubsequence(word):
            prev = -1
            
            for c in word:
                if c not in index_map:
                    return False
                
                index = bisect_right(index_map[c], prev)
                
                if index == len(index_map[c]):
                    return False
                
                prev = index_map[c][index]
                
            return True
        
        
        index_map = defaultdict(list)

        for i, c in enumerate(s):
            index_map[c].append(i)

            
                
            
        ans = 0
        for w in words:
            if isSubsequence(w):
                ans += 1 

        return ans