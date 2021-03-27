#https://leetcode.com/problems/jewels-and-stones/

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        return [ 1 for stone in stones if stone in jewels ].__len__()