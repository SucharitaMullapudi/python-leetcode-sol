class Solution(object):
    def sortArrayByParity(self, A):
        result = []
        for i in range(len(A)):
            if A[i]%2 ==0:
                result.insert(0,A[i])
            else:
                result.append(A[i])       
        return result
