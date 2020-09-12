class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result = []
        # nums.sort()
        # for index in range(len(nums)):
        #     if nums[index] in nums[index+1:]:
        #         result.append(nums[index])
        # return result
        from collections import Counter
        diff =list((Counter(nums)- Counter(list(set(nums)))).elements())
        return diff
