#https://leetcode.com/problems/lemonade-change/

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
                continue
            if bill == 10:
                ten += 1
                if five:
                    five -= 1
                else:
                    return False
                continue
            if bill == 20:
                if five and ten:
                    five -= 1
                    ten -= 1
                elif five > 2:
                    five -= 3
                else:
                    return False
        return True