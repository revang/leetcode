#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

from typing import List

# @lc code=start

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        for i in range(k):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        res = [nums[dq[0]]]
        for i in range(k, len(nums)):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            while dq[0] <= i-k:
                dq.popleft()
            res.append(nums[dq[0]])

        return res


# @lc code=end
def test():
    assert Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3) == [3, 3, 5, 5, 6, 7]
    assert Solution().maxSlidingWindow(nums=[1], k=1) == [1]
    assert Solution().maxSlidingWindow(nums=[1, -1], k=1) == [1, -1]
    assert Solution().maxSlidingWindow(nums=[7, 2, 4], k=2) == [7, 4]
