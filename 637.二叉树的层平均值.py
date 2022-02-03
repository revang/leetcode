#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

from typing import Optional, List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

    def __repr__(self):
        """ print的时候打印自定义的值 """
        return "<Node: {}>".format(self.val)

# @lc code=start


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        res = []
        cur_nodes = [root]
        while cur_nodes:
            # print(cur_nodes)
            next_nodes = []
            sum, count = 0, 0
            for node in cur_nodes:
                sum += node.val
                count += 1
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            res.append((sum/count))
            cur_nodes = next_nodes
        return res

# @lc code=end


def test():
    assert Solution().averageOfLevels(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == [3, 14.5, 11]
