#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            ans = []
            for _ in range(size):
                node = queue.popleft()
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans[0]


# @lc code=end

def test():
    root = init_tree([2, 1, 3])
    ans = Solution().findBottomLeftValue(root)
    print(ans)
    assert ans == 1

    root = init_tree([1, 2, 3, 4, None, 5, 6, None, None, 7])
    ans = Solution().findBottomLeftValue(root)
    print(ans)
    assert ans == 7
