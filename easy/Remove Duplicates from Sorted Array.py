class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i < len(nums):
            a = nums[i]
            j = i+1
            while j <len(nums):
                if a == nums[j]:
                    nums.pop(j)
                    j -=1
                j +=1
            i+=1
