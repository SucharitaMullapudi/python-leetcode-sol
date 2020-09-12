class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diction = {}
        res = []
        set_nums = list(set(nums))
        for i in range(len(set_nums)):
            diction[set_nums[i]]=0
            for index in range(len(nums)):
                if set_nums[i] == nums[index]:
                    diction[set_nums[i]] +=1
        for i in range(len(set_nums)):
            if diction[set_nums[i]] > len(nums)/3:
                res.append(set_nums[i])
        return res
                
