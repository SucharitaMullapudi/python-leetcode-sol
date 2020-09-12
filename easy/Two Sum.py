class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        summ = 0
        list1=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                summ = nums[i]+nums[j]
                if summ == target:
                    list1.append(i)
                    list1.append(j)
        return list1
