#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1比特与2比特字符
#

from typing import List
from collections import deque

# @lc code=start


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        queue = deque(bits)
        while len(queue) >= 2:
            if queue[0] == 1:
                queue.popleft()
                queue.popleft()
            else:
                queue.popleft()
        return len(queue) == 1 and queue[0] == 0

# @lc code=end


def test():
    assert Solution().isOneBitCharacter([1, 0, 0]) == True
