#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

from typing import List
from collections import defaultdict

# @lc code=start


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = defaultdict(int)
        for num in nums:
            hashtable[num] = hashtable[num]+1
        return max(hashtable.values()) > 1

# @lc code=end


def test():
    assert Solution().containsDuplicate([1, 2, 3, 1]) == True
