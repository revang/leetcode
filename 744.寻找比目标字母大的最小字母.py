#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *

# @lc code=start


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]

        left, right = 0, len(letters)-1
        while left < right:
            mid = (left+right)//2
            if letters[mid] <= target:
                left = mid+1
            else:
                right = mid
        return letters[left]

# @lc code=end
