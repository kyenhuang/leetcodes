#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#


# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        1, 判断和是否有三个元素和为0
        2，返回数组
        3，判断数组是否重复
        
        双指针的使用
        去掉重复的元组， 可以先排序避免
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            # 从小到大搜索， 跳过重复值
            if (i > 0 and nums[i] == nums[i - 1]):
                continue

            # 左指针
            l = i + 1
            # 右指针
            r = len(nums) - 1

            while (l < r):

                if (nums[i] + nums[l] + nums[r] == 0):
                    # 如果三个数相加等于0 加入到结果
                    res.append([nums[i], nums[l], nums[r]])
                    while (l < r and nums[l] == nums[l + 1]):
                        # 如果左指针重复 后移
                        l = l + 1
                    while (l < r and nums[r] == nums[r - 1]):
                        # 如果右指针重复， 后移
                        r = r - 1
                    # 如果都不是 双指针同时移动
                    l = l + 1
                    r = r - 1

                elif (nums[i] + nums[l] + nums[r] > 0):
                    r = r - 1
                else:
                    l = l + 1

        return res


# @lc code=end
