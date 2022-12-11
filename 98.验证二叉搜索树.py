#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        证明中序遍历为升序
        """
        stack = deque()
        stack.append((root, False))

        # 记录中序遍历前一个值
        inorder = float("-inf")

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    if cur.val <= inorder:
                        return False
                    inorder = cur.val
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

        return True


# @lc code=end
def test():
    assert Solution().isValidBST(create_tree([2, 1, 3])) == True
    assert Solution().isValidBST(create_tree([2, 2, 2])) == False
    assert Solution().isValidBST(create_tree([5, 4, 6, None, None, 3, 7])) == False
