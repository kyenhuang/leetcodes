#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        Check x is positive or not, if yes, return false
        """
        if x < 0:
            return False
        
        cur = 0
        num = x
        while (num != 0):
            cur = cur * 10 + num % 10 
            num /= 10

        return cur == x

    
        
        

# @lc code=end

