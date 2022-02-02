#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

from typing import List

# @lc code=start


# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         for num in nums:
#             if num == target:
#                 return True
#         return False

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start+int((end-start)/2)
            if nums[mid] == target:
                return True
            if nums[start] == nums[mid]:
                start += 1
                continue
            if nums[start] < nums[mid]:  # 前半部分有序
                if nums[start] <= target < nums[mid]:  # target在前半部分
                    end = mid-1
                else:  # 否则去后半部分找
                    start = mid+1
            else:  # 后半部分有序
                if nums[mid] < target <= nums[end]:  # target在后半部分
                    start = mid+1
                else:  # 否则去前半部分找
                    end = mid-1
        return False  # 一直没找到，返回false

# @lc code=end


def test():
    assert Solution().search([2, 5, 6, 0, 0, 1, 2], 0) == True
    assert Solution().search([2, 5, 6, 0, 0, 1, 2], 3) == False
    assert Solution().search([1, 0, 1, 1, 1], 0) == True
    assert Solution().search([1], 0) == False
