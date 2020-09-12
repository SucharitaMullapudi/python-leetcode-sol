class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = max(nums)
        index = nums.index(b)
        nums.pop(index)
        a = max(nums)
        return (a-1)*(b-1)
