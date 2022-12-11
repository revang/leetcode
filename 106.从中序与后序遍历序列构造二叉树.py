#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        # 确定根节点
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 查找根节点在中序遍历序列中的位置
        root_idx = inorder.index(root_val)

        # 构造左子树和右子树
        root.left = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = self.buildTree(inorder[root_idx+1:], postorder[root_idx:-1])

        return root

# @lc code=end


def test():
    assert is_same_tree(Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]), Tree([3, 9, 20, None, None, 15, 7]).root)
