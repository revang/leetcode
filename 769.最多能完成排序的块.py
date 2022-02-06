#
# @lc app=leetcode.cn id=769 lang=python3
#
# [769] 最多能完成排序的块
#

from typing import List

# @lc code=start


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks, cur_max = 0, 0
        for i in range(len(arr)):
            cur_max = max(cur_max, arr[i])
            if cur_max == i:
                chunks += 1
        return chunks

# @lc code=end


def test():
    assert Solution().maxChunksToSorted([4, 3, 2, 1, 0]) == 1
    assert Solution().maxChunksToSorted([1, 0, 2, 3, 4]) == 4
