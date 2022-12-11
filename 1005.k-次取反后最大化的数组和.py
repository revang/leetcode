#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

import heapq
from typing import List

# @lc code=start


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        minheap = nums
        heapq.heapify(minheap)

        for _ in range(k):
            val = heapq.heappop(minheap)
            val = -val
            heapq.heappush(minheap, val)

        return sum(minheap)


# @lc code=end
def test():
    assert Solution().largestSumAfterKNegations(nums=[4, 2, 3], k=1) == 5
    assert Solution().largestSumAfterKNegations(nums=[3, -1, 0, 2], k=3) == 6
    assert Solution().largestSumAfterKNegations(nums=[2, -3, -1, 5, -4], k=2) == 13
