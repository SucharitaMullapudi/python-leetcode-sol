class Solution(object):
    def shuffle(self, nums, n):
        leng = len(nums)/2
        a=[]
        b=[]
        c=[]
        for index in range(leng):
            a.append(nums[index])
        for index in range(leng,len(nums)):
            b.append(nums[index])
        for index in range(leng):
            c.append(a[index])
            c.append(b[index])
        return c
