class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        a=[]
        for index in range(len(nums)):           
            count = 0
            for j in range(len(nums)):
                if nums[index]>nums[j]:
                    count +=1
                else:
                    pass
            a.append(int(count))
        return a
