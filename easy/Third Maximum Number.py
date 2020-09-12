class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums)==0:
            return 0
        elif len(nums)==1 or len(nums)==2:
            return max(nums)
        else:
            nums.pop(nums.index(max(nums)))
            nums.pop(nums.index(max(nums)))
            return max(nums)
