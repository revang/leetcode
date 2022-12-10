#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

from leetcode_tool import *


# @lc code=start


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSymmetric(left: TreeNode, right: TreeNode):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return isSymmetric(left.left, right.right) and isSymmetric(left.right, right.left)

        return isSymmetric(root.left, root.right)

# @lc code=end


def test():
    assert Solution().isSymmetric(Tree([1, 2, 2, 3, 4, 4, 3]).root) == True
    assert Solution().isSymmetric(Tree([1, 2, 2, None, 3, None, 3]).root) == False
