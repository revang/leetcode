#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_cnt, max_val = 0, []
        pre_cnt, pre_val = 0, None

        stack = deque()
        stack.append((root, False))

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    if cur.val == pre_val:
                        pre_cnt += 1
                    else:
                        pre_cnt = 1
                        pre_val = cur.val

                    if pre_cnt > max_cnt:
                        max_cnt, max_val = pre_cnt, [pre_val]
                    if pre_cnt == max_cnt and pre_val not in max_val:
                        max_val.append(pre_val)

                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

        return max_val

# @lc code=end


def test():
    assert Solution().findMode(create_tree([1, None, 2, 2])) == [2]
