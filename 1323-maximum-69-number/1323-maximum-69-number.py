class Solution:
    def maximum69Number (self, num: int) -> int:
        numbers = list(str(num))
        for i, n in enumerate(numbers):
            if n != '9':
                numbers[i] = '9'
                break
        
        return int("".join(numbers))
        