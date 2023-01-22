class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def dfs(s, path, res):
            if not s:
                res.append(path)
                
            for i in range(1, len(s)+1):
                if is_palindrome(s[:i]):
                    dfs(s[i:], path+[s[:i]], res)
        
        def is_palindrome(string):
            return string == string[::-1]
        
        
        res = []
        dfs(s, [], res)
        return res
                
