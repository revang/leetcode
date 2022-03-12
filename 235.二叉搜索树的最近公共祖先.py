#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

from typing import Optional
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestor = root  # ancestor 祖先
        while ancestor:
            if ancestor.val < p.val and ancestor.val < q.val:
                ancestor = ancestor.right
            elif ancestor.val > p.val and ancestor.val > q.val:
                ancestor = ancestor.left
            else:
                break
        return ancestor

# @lc code=end


def test():
    root = init_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    ans = Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(8))
    print(ans)
    assert ans.val == 6

    root = init_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    ans = Solution().lowestCommonAncestor(root, TreeNode(2), TreeNode(4))
    print(ans)
    assert ans.val == 2
