class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        
        for v in (2,3,5):
            if(n%v==0):
                while(n%v==0):
                    n=n//v
        
        return n==1