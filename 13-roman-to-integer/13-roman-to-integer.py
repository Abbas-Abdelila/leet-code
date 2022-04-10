class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I":1, "V":5, "X":10,"L":50, "C":100, "D":500, "M":1000}
        prev_num = 0
        total=0
        for x in s[::-1]:
            if(roman[x] >= prev_num):
                total+=roman[x]
            else:
                total-=roman[x]
            prev_num = roman[x]
        
        return total
        