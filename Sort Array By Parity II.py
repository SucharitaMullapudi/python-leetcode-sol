class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        a=[None]*(len(A))
        n=0
        n1=1
        for i in range(len(A)):
            if A[i]%2 ==0:
                a[n] =A[i]
                n +=2
            else:
                a[n1] =A[i]
                n1+=2
        return a
