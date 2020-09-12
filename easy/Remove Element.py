class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums)):
            if val in nums: 
                nums.pop(nums.index(val))
        return len(nums)
