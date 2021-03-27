#https://leetcode.com/problems/third-maximum-number/

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = two = three = -sys.maxint
        for num in nums:
            if num > one:
                one, two, three = num, one, two
            elif num > two and num < one:
                two, three = num, two
            elif num > three and num < two:
                three = num
        return three if three != -sys.maxint else one