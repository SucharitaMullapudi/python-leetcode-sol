class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result = []
        # for num in range(1,len(nums)+1):
        #     if num not in nums:
        #         result.append(num)
        # return result
        diff = list(set(range(1,len(nums)+1))-set(nums))
        return diff
