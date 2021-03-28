#https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        for i in range( 1, len( arr ) ):
            if arr[ i ] > arr[ i + 1 ]:
                return i