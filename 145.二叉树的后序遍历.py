#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = deque()
        stack.append((root, False))

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    res.append(cur.val)
                else:
                    stack.append((cur, True))
                    stack.append((cur.right, False))
                    stack.append((cur.left, False))
        return res


# @lc code=end

def test():
    assert Solution().postorderTraversal(Tree([1, None, 2, 3]).root) == [3, 2, 1]
