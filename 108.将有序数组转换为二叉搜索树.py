#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sortedArrayToBST(left, right):
            if left > right:
                return

            # 选择中间位置，向0取整, mid计算从0开始
            mid = int(left+(right-left)/2)

            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(left, mid-1)
            root.right = sortedArrayToBST(mid+1, right)
            return root

        return sortedArrayToBST(0, len(nums)-1)


# @lc code=end
def test():
    print_tree(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))
