class Solution(object):
    def runningSum(self, nums):
        self.nums = nums
        for index in range(1,len(nums)):
            nums[index] = nums[index]+nums[index-1]
        return nums
