#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#

from typing import List
# @lc code=start


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        while start < end:
            mid = start+(end-start)//2
            if nums[mid] == nums[mid-1]:
                if (mid-start-1) % 2 == 0:  # 左边是偶数, 那么单一元素在右边
                    start = mid+1
                else:
                    end = mid-2
            elif nums[mid] == nums[mid+1]:
                if (mid-start) % 2 == 0:
                    start = mid+2
                else:
                    end = mid-1
            else:
                return nums[mid]
        return nums[start]

# @lc code=end


def test():
    assert Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    assert Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10
