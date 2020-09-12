class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        com_text = ['b','a','l','l','o','o','n']
        count = 0
        text = list(text)
        check = True
        while len(text)>=7:
            for i in com_text:
                if i in text:
                    text.remove(i)
                    count+=1
                else:
                    check = False
            if check ==False:
                break
        return count/7
