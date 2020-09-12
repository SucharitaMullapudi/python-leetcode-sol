class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        import decimal
        a = salary.index(min(salary))
        salary.pop(a)
        b = salary.index(max(salary))     
        salary.pop(b)
        return decimal.Decimal(sum(salary))/len(salary)
