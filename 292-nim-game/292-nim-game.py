class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Ask when can I not win? When you are left with 4 stones. So you don't wanna get 
        # 4 remaining but for the rest since you are the beginner, መቀመር ትችላለ ፡፡
        # 4'ትን ማየት አትፈልግም!
        
        return (n % 4 != 0)
        