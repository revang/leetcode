#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

    def __repr__(self):
        return "<Node: {}>".format(self.val)


def init_tree(values):
    queue = deque()
    root = None

    if values:
        root = TreeNode(values[0])
        queue.append(root)

    index = 1
    while index < len(values):
        node = queue.popleft()

        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root


def print_tree(root):
    if not root:
        return
    cur_nodes = [root]
    while cur_nodes or next_nodes:
        print(cur_nodes)
        next_nodes = []
        for node in cur_nodes:
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)
        cur_nodes = next_nodes

# @lc code=start


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return
        root_val = preorder[0]  # root节点的值
        root_idx_inorder = inorder.index(root_val)  # 中序遍历root节点的位置
        left_size = root_idx_inorder  # root.left节点长度(从中序遍历可知)
        left_part = self.buildTree(preorder[1:left_size+1], inorder[0:left_size])
        right_part = self.buildTree(preorder[left_size+1:], inorder[left_size+1:])
        return TreeNode(root_val, left_part, right_part)


# @lc code=end

def test():
    ans = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print_tree(ans)
