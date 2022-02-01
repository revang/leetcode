#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

"""
author : revang
date   : 2022-02-01
method : 哈希表
"""

from typing import List

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for idx, val in enumerate(nums):
            pair_val = target-val
            if pair_val in hashtable:
                return [hashtable[pair_val], idx]
            hashtable[val] = idx
        return []

# @lc code=end


def test():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
