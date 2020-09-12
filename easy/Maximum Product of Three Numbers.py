class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = max(nums)
        nums.pop(nums.index(b))
        a = max(nums)
        nums.pop(nums.index(a))
        c = max(nums) 
        nums.pop(nums.index(c))  
        if len(nums)==0:
            return a*b*c
        elif len(nums) ==1:
            d = min(nums)
            nums.pop(nums.index(d))
            return a*b*c
        else:
            d = min(nums)
            nums.pop(nums.index(d))
            e = min(nums)
            nums.pop(nums.index(e)) 
            return max(a*b*c,b*d*e)
