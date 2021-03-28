#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, p, i = 0, 1, 0
        while n > 0:
            i = n % 10
            n = n / 10
            s += i
            p *= i
        return p - s