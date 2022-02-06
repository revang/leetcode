#
# @lc app=leetcode.cn id=1110 lang=python3
#
# [1110] 删点成林
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
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        ds = set(to_delete)
        root = self.process(root, ds, ans)
        if root:
            ans.append(root)
        return ans

    def process(self, root, ds, ans):
        if root is None:
            return
        root.left = self.process(root.left, ds, ans)
        root.right = self.process(root.right, ds, ans)
        if root.val not in ds:
            return root
        if root.left:
            ans.append(root.left)
        if root.right:
            ans.append(root.right)
        return


# @lc code=end

def test():
    root = init_tree([1, 2, 3, 4, 5, 6, 7])
    ans = Solution().delNodes(root, [3, 5])
    for item in ans:
        print("item: ")
        print_tree(item)
