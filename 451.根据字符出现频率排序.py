#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        hashtable = defaultdict(int)
        for char in s:
            hashtable[char] += 1

        sorted_list = sorted(hashtable.items(), key=lambda x: x[1], reverse=True)
        res = ""
        for item in sorted_list:
            res += item[0]*item[1]
        return res

# @lc code=end


def test():
    assert Solution().frequencySort("tree") in ("eert", "eetr")
    assert Solution().frequencySort("cccaaa") == "cccaaa"
    assert Solution().frequencySort("Aabb") == "bbAa"
