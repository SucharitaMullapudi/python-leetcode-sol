class Solution(object):
    def balancedStringSplit(self, s):
        count = 0
        result =0
        for index in range(len(s)):
            if s[index] == 'R':
                count += -1
            elif s[index] =='L':
                count += 1
            if count == 0:
                result +=1
        return result
