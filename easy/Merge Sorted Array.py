class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        a = n
        while n>0:
            nums1.pop(-1)
            n -=1
        for i in range(a):
            nums1.append(nums2[i])
        nums1.sort()
