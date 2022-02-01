#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

"""
author : revang
date   : 2022-02-01
method : 排序+双指针
"""


from typing import List

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []

        nums.sort()
        size = len(nums)
        ans = []
        for i in range(size-2):
            left, right = i+1, size-1
            while left < right:
                val = nums[i]+nums[left]+nums[right]
                if val == 0:
                    item = [nums[i], nums[left], nums[right]]
                    if item not in ans:
                        ans.append(item)
                    left += 1
                    right -= 1
                elif val < 0:
                    left += 1
                else:
                    right -= 1
        return ans

# @lc code=end


def test():
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert Solution().threeSum([]) == []
