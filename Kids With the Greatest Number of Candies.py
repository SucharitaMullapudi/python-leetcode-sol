class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        a=[]
        c=[]
        high = max(candies)
        for i in candies:
            b = i+extraCandies
            a.append(b)
        for num in a:
            if num>=high:
                c.append(True)
            else:
                c.append(False) 
        return c
