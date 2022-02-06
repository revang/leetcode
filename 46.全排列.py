#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

from typing import List

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(nums, begin, end):
            if begin == end:
                ans.append(nums[:])
                return
            for i in range(begin, end+1):
                nums[i], nums[begin] = nums[begin], nums[i]  # 修改当前节点状态
                backtrack(nums, begin+1, end)  # 递归子节点
                nums[i], nums[begin] = nums[begin], nums[i]  # 回改当前节点状态

        backtrack(nums, 0, len(nums)-1)
        return ans

# @lc code=end


def testSolution():
    assert len(Solution().permute([1, 2, 3])) == 6
