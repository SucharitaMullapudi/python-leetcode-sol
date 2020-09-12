class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        empty_list = []
        duplicate_list = []
        for index in range(len(nums)):
            a = nums[index]
            if a not in empty_list:
                empty_list.append(a)
            else:
                duplicate_list.append(a)
        diff = set(nums)- set(duplicate_list)
        return (list(diff))
        
