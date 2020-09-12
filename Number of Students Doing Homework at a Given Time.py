class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        count=0
        for i in range(len(startTime)):
            a = []
            a.append(startTime[i])
            a.append(endTime[i])
            if queryTime in range(a[0],a[1]+1):
                count +=1
            else:
                pass
        del a[:]
        return count
