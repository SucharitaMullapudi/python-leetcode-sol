class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_a=0
        count_l=0
        for i in range(len(s)):
            if s[i] == 'A':
                count_a +=1
        for i in range(len(s)-2):
            if s[i] == 'L':
                if s[i+1]=='L':
                    if s[i+2]=='L':
                        count_l +=1
        if count_l >=1 or count_a >1:
            return False
        else:
            return True
