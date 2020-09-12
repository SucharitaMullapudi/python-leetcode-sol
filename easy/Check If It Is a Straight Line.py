class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        i = 2
        if len(coordinates)==2 :
            m = (y2-y1)/(x2-x1)
            if (y2-y1) == m*(x2-x1):
                return True
            else:
                return False
        elif (len(coordinates)==3) and (x1 ==0 and y1 ==0):
            x3 = coordinates[i][0]
            y3 = coordinates[i][1]
            if (abs(y3) == abs(y2)) or (abs(x3) == abs(x2)):
                return True
            else:
                return False
        else:
            count =0
            while i in range(2,len(coordinates)):
                x3 = coordinates[i][0]
                y3 = coordinates[i][1]
                if (x1 ==x2 == x3) or (y1 == y2 == y3):
                    count +=1
                elif (x2-x1) == 0 or (y2-y1) ==0:
                    pass
                elif ((x3-x1)/(x2-x1)) == ((y3-y1)/(y2-y1)):
                    count +=1
                i+=1
        del i
        if count == len(coordinates)-2:
            return True
        else:
            return False
