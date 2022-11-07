class Solution:
    def maximum69Number (self, num: int) -> int:
        n = num
        for i in reversed(range(4)): # range(4, 0, -1)
            d, n = divmod(n, 10**i)
            if d == 6:
                return num + 3*10**i # adds three to the respective 10th place
        return num     
        
        
        # -> With string
#         numbers = list(str(num))
#         for i, n in enumerate(numbers):
#             if n != '9':
#                 numbers[i] = '9'
#                 break
        
#         return int("".join(numbers))
        