class Solution(object):
    def sumZero(self, n):
        empty_list = []
        i = 1
        if n%2 !=0:
            while i <= n//2:
                empty_list.append(i)
                empty_list.append(-i)
                i+=1
            empty_list.append(0)
        elif n ==1:
            empty_list.append(0)
        else:
            while i <= n//2:
                empty_list.append(i)
                empty_list.append(-i)
                i+=1
        return empty_list
