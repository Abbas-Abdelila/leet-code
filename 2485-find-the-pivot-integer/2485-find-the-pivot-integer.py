class Solution:
    def pivotInteger(self, n: int) -> int:
        def calc_sum(start, end):
            return ((end-start)+1) / 2 * (start + end)
        

        for i in range(1, n+1):
            if calc_sum(1,i) == calc_sum(i, n):
                return i
        
        return -1