class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in range(1,len(nums)+2):
            if num not in nums:
                if num <=0:
                    pass
                else:
                    return num
