#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        max_val = max(nums)
        max_idx = nums.index(max_val)
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        return root

# @lc code=end


def test():
    assert is_same_tree(Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]), create_tree([6, 3, 5, None, 2, 0, None, None, 1])) == True
