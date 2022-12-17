#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        cur_row = [1]
        for i in range(1, rowIndex+1):
            next_row = [1]
            for j in range(1, i):
                next_row.append(cur_row[j-1]+cur_row[j])
            next_row.append(1)
            cur_row = next_row
        return cur_row

# @lc code=end


def test():
    assert Solution().getRow(3) == [1, 3, 3, 1]
