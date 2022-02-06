#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

from typing import List

# @lc code=start


class NumArray:
    def __init__(self, nums: List[int]):
        self.items = nums
        self.sum_items = [0]
        for idx, val in enumerate(self.items):
            if idx == 0:
                self.sum_items.append(val)
            else:
                self.sum_items.append(self.sum_items[-1]+val)

    def sumRange(self, left: int, right: int) -> int:
        return self.sum_items[right+1]-self.sum_items[left]

# @lc code=end


def test():
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    assert numArray.sumRange(0, 2) == 1
    assert numArray.sumRange(2, 5) == -1
    assert numArray.sumRange(0, 5) == -3
