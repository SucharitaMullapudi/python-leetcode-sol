class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """  
        s = list(s)
        for i in list(t):
            if i in s:
                s.remove(i)
            else:
                return str(i)
