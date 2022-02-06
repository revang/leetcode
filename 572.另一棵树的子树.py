#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
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


# @lc code=start

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        return self.isSubtreeHelper(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSubtreeHelper(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        return root.val == subRoot.val and self.isSubtreeHelper(root.left, subRoot.left) and self.isSubtreeHelper(root.right, subRoot.right)

# @lc code=end


def test():
    print("testcase 1")
    root = init_tree([3, 4, 5, 1, 2])
    subRoot = init_tree([4, 1, 2])
    ans = Solution().isSubtree(root, subRoot)
    assert ans == True
    print(ans)

    print("testcase 2")
    root = init_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    subRoot = init_tree([4, 1, 2])
    ans = Solution().isSubtree(root, subRoot)
    assert ans == False
    print(ans)

    print("testcase 3")
    root = init_tree([1, 1])
    subRoot = init_tree([1])
    ans = Solution().isSubtree(root, subRoot)
    assert ans == True
    print(ans)

    print("testcase 4")
    root = init_tree([3, 4, 5, 1, None, 2])
    subRoot = init_tree([3, 1, 2])
    ans = Solution().isSubtree(root, subRoot)
    assert ans == False
    print(ans)
