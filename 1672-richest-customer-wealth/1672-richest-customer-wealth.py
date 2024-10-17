class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        biggest = 0
        for l in accounts:
            sumn = 0
            for num in l:
                sumn = sumn + num
            if (sumn > biggest):
                biggest = sumn
        return biggest