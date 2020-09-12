class Solution(object):
    def xorOperation(self, n, start):
        from operator import ixor 
        nums = [None]*n
        for i in range(n):
            nums[i]=start+2*i
        return reduce(ixor,nums)
