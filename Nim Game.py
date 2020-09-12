class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n in (1,2,3):
            return True
        elif n%4 ==0:
            return False
        elif n%5==0 or n%6 ==0 or n %7==0 or n%8 ==0 or n%9==0:
            return True
        else: 
            return True
