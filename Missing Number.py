class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1 and max(nums) >1 :
                    return max(nums)+1
        else:    
            for i in range(len(nums)+1):
                if i not in nums:
                    return i
