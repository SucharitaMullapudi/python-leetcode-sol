class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        import copy
        n = copy.copy(num)
        num_2 =[]
        num = list(map(int,str(num))) 
        for index in range(len(num)):
            new_num =copy.copy(num)
            if num[index] ==6:
                new_num[index]=9
            else:
                new_num[index]=6
            result = int(''.join(map(str,new_num)))
            print(result)
            num_2.append(result)
        print(num_2)
        
        for index in range(len(num_2)):            
            if n > num_2[index]:
                print(n)
            else:
                n = copy.copy(num_2[index])
        return n
