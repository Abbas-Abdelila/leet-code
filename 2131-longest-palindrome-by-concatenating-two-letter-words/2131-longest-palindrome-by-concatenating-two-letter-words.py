class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = defaultdict(int)
        unpaired = ans = 0

        for word in words:
            if word[0] == word[1]:
                if d[word] > 0:
                    d[word] -= 1
                    unpaired -= 1
                    ans += 4
                else:
                    d[word] += 1
                    unpaired += 1
            else: # letters are different
                if d[word[::-1]] > 0:
                    d[word[::-1]] -= 1
                    ans += 4
                else:
                    d[word] += 1
        
        if unpaired > 0:
            ans += 2
        return ans
