#
# @lc app=leetcode.cn id=136 lang=python
#
# [136] 只出现一次的数字
#

# @lc code=start

import collections
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # dic = collections.Counter(nums)

        # for key, vla in dic.items():
        #     if vla == 1:
        #         return key

        """
        通过列表完成
        python： 列表.count(element)
        """
        if len(nums) == 1:
            return nums[0]

        for i in nums:
            res = nums.count(i)
            if res == 1:
                return i


            
            

        

# @lc code=end

