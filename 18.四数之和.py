#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

"""
author : revang
date   : 2022-02-01
method : 排序+双指针
"""


from typing import List

# @lc code=start


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []

        nums.sort()
        size = len(nums)
        ans = []
        for i in range(size-3):
            for j in range(3, size):
                left, right = i+1, j-1
                while i < left < right < j:
                    val = nums[i]+nums[left]+nums[right]+nums[j]
                    if val == target:
                        item = [nums[i], nums[left], nums[right], nums[j]]
                        if item not in ans:
                            ans.append(item)
                        left += 1
                        right -= 1
                    elif val < target:
                        left += 1
                    else:
                        right -= 1
        return ans

# @lc code=end


def test():
    assert Solution().fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert Solution().fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
    assert Solution().fourSum([0], 0) == []
