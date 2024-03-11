class Solution:
    def customSortString(self, order: str, s: str) -> str:
        my_dict = {}
        for idx, char in enumerate(order):
            my_dict[char] = 204 - idx
        
        result = []
        suffix = []
        for char in s:
            if char in my_dict:
                result.append((char, my_dict[char]))
            else: 
                suffix.append(char)
        
        result = [x[0] for x in sorted(result, key=lambda x:x[1], reverse=True)]
        
        return "".join(result) + "".join(suffix)
