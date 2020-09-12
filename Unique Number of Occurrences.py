class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        set_arr = list(set(arr))
        empty_arr = []       
        for i in set_arr:
            count =0
            for j in range(len(arr)):
                if i == arr[j]:
                    count+=1
                else:
                    pass
            empty_arr.append(count)
        if len(empty_arr) == len(list(set(empty_arr))):
            return True
        else:
            return False
