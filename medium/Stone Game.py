class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        while True:
            adding_alex = []
            adding_lee = []
            for index in piles:
                init = piles[0]
                end  = piles[-1]
                maxy = max(init,end)
                mini = min(init,end)
                adding_alex.append(maxy)
                adding_lee.append(mini)
                piles.pop(0)
                piles.pop(-1)
                if piles == []:
                    if sum(adding_alex) > sum(adding_lee):
                        return True
                        break
                    else:
                        return False
