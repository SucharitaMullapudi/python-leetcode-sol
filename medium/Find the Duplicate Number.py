class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        empty_list = []
        for index in range(len(nums)):
            if nums[index] not in empty_list:
                empty_list.append(nums[index])
            else:
                # del empty_list
                return nums[index]
