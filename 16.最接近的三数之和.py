#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

"""
author : revang
date   : 2022-02-01
method : 排序+双指针
"""


from typing import List

# @lc code=start


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return -1

        nums.sort()
        size = len(nums)
        ans = sum(nums[0:3])
        for i in range(size-1):
            left, right = i+1, size-1
            while left < right:
                val = nums[i]+nums[left]+nums[right]
                if val == target:
                    return target
                elif val < target:
                    if abs(val-target) < abs(ans-target):
                        ans = val
                    left += 1
                else:
                    if abs(val-target) < abs(ans-target):
                        ans = val
                    right -= 1
                    continue
        return ans

# @lc code=end


def test():
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert Solution().threeSumClosest([0, 0, 0], 1) == 0
