class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = list(s)
        if len(st) ==1:
            return 0
        rep = []
        common =[]
        for i in st:
            if i not in rep:
                rep.append(i)
            else:
                common.append(i)
        for i in list(set(common)):
            rep.remove(i)
        if len(rep)>=1:
            res = st.index(rep[0])
        else:
            res =-1
        return res
        
