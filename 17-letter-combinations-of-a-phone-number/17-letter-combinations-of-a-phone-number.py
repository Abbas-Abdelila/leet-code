class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dictionary = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        N = len(digits)
        
        if N==0:
            return []
        
        ans = []
        
        def recurse(index, current):
            if index == N:
                ans.append("".join(current))
                return
            
            for c in dictionary[digits[index]]:
                current.append(c)
                recurse(index+1, current)
                current.pop()
                
        
        recurse(0, [])
        return ans