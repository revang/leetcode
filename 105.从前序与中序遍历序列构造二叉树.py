#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None

        # 确定根节点
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 查找根节点在中序遍历序列中的位置
        root_idx = inorder.index(root_val)

        # 构造左子树和右子树
        root.left = self.buildTree(preorder[1:1 + root_idx], inorder[:root_idx])
        root.right = self.buildTree(preorder[1 + root_idx:], inorder[root_idx + 1:])

        return root


# @lc code=end

def test():
    assert is_same_tree(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]), Tree([3, 9, 20, None, None, 15, 7]).root)
