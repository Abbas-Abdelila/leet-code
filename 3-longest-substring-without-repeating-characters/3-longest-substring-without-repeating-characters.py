class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start = 0
        seen = set()
        max_so_far = 0
        end = 0
        while end <= len(s) - 1:
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
            max_so_far = max(max_so_far, end - start + 1)
            end += 1
        return max_so_far