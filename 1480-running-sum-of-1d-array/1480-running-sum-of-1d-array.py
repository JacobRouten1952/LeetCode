class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 0
        count = 0
        runningsum = []
        for x in nums:
            total = total + nums[count]
            runningsum.append(total)
            count = count + 1
            
        return runningsum
        