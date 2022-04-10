class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        for i in digits:
            s = s+str(i)
        a = int(s)+1
        
        return [int(x) for x in str(a)]
        