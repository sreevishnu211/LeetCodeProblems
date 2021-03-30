#https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0]
        interimCount = 1
        if not nums:
            return 0
        for i in range( 1, len( nums ) ):
            if nums[ i ] > nums[ i - 1 ]:
                interimCount += 1
            else:
                count.append( interimCount )
                interimCount = 1
        count.append( interimCount )
        return max( count )