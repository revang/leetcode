#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

from typing import List

# @lc code=start


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                cur_num = num
                cur_count = 1
                while cur_num+1 in num_set:
                    cur_num += 1
                    cur_count += 1
                res = max(res, cur_count)
        return res

# @lc code=end


def test():
    assert Solution().longestConsecutive(nums=[100, 4, 200, 1, 3, 2]) == 4
