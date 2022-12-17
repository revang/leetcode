#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        cur_row = [1]
        all_rows = [cur_row]
        for i in range(1, numRows):
            next_row = [1]
            for j in range(1, i):
                next_row.append(cur_row[j-1]+cur_row[j])
            next_row.append(1)

            all_rows.append(next_row)
            cur_row = next_row

        return all_rows


# @lc code=end
def test():
    assert Solution().generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
