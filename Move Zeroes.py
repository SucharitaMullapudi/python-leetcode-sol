class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=0
        i=0
        while i <len(nums):
            if nums[i]==0:
                count +=1
            i+=1
        while 0 in nums:
            nums.remove(0)    
        i=0
        while i<count:
            nums.append(0)
            i+=1
