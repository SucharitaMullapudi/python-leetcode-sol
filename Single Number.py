class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        empty_list = []
        a = []
        for i in nums:
            if i not in empty_list:
                empty_list.append(i)
            else:
                a.append(i)
        nums = list(set(empty_list)-set(a))
        return nums[0]
