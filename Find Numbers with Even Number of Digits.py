class Solution(object):
    def findNumbers(self, nums):
        new_list = []
        count = []
        n=0
        for i in range(len(nums)):
            new_list.append(list(str(nums[i])))
        for index in range(len(new_list)):
            count.append(len(new_list[index]))
        print(count)
        for i in count:
            if i%2==0:
                n+=1
            else:
                pass
        return n
