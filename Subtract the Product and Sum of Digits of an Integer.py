class Solution(object):
    def subtractProductAndSum(self, n):
        digits = [int(i) for i in str(n)]
        i=1
        j=0
        for d in digits:
            i*=d
            j+=d
        return i-j
