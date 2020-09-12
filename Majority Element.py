class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        diction = {}
        set_nums = list(set(nums))
        for i in range(len(set_nums)):
            diction[set_nums[i]]=0
            for index in range(len(nums)):
                if set_nums[i] == nums[index]:
                    diction[set_nums[i]] +=1
        for i in range(len(set_nums)):
            if diction[set_nums[i]] >len(nums)/2:
                return set_nums[i]
