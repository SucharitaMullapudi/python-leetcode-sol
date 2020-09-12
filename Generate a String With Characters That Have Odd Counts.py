class Solution(object):
    def generateTheString(self, n):
        if n%2==0:
            string = (n-1)*'a'+'b'
        else:
            string = n*'a'
        return string
