#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

import heapq
from typing import List
from collections import defaultdict

# @lc code=start


# 桶排序(哈希表)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = defaultdict(int)
        for num in nums:
            hashtable[num] += 1
        sorted_list = sorted(hashtable.items(), key=lambda x: x[1], reverse=True)
        idx = 0
        res = []
        while idx < k:
            res.append(sorted_list[idx][0])
            idx += 1
        return res

# @lc code=end


def test():
    assert Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert Solution().topKFrequent([1], 1) == [1]
