#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

from typing import List, Optional
from collections import deque, defaultdict
from leetcode_tool import *

# @lc code=start


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            line = image[i]
            line = line[::-1]
            line = [(x+1) % 2 for x in line]
            image[i] = line
        return image

# @lc code=end


def test():
    assert Solution().flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]) == [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
