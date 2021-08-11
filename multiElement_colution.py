#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#

# @lc code=start
import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        dics = collections.Counter(nums)
        for key, val in dics.items():
            if val > len(nums) / 2:
                return key

        


# @lc code=end

