#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

"""
author : revang
date   : 2022-02-02
method : 贪心-相邻问题
"""

from typing import List

# @lc code=start


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, size, pre = 0, len(flowerbed), -1
        for i in range(size):
            if flowerbed[i] == 1:
                if pre < 0:
                    count += i//2
                else:
                    count += (i-pre-2)//2
                pre = i
        if pre < 0:
            count += (size+1)//2
        else:
            count += (size-pre-1)//2
        return count >= n

# @lc code=end


def test():
    assert Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1) == True
    assert Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2) == False
    assert Solution().canPlaceFlowers([1, 0, 0, 0, 0], 2) == True
    assert Solution().canPlaceFlowers([1, 0, 0, 1, 0], 2) == False
    assert Solution().canPlaceFlowers([0, 1, 0], 1) == False
    assert Solution().canPlaceFlowers([0, 0, 0, 0], 3) == False
