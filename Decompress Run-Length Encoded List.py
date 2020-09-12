class Solution(object):
    def decompressRLElist(self, nums):
        list1 =[]
        index = 0
        while index < len(nums):
            freq = nums[index]
            val = nums[index+1]
            list1 = list1+[val]*freq
            index +=2
        return list1
