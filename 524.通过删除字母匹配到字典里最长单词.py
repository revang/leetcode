#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#

from typing import List

# @lc code=start

from collections import Counter


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ""
        for item in dictionary:
            i, j = 0, 0
            while i < len(item) and j < len(s):
                if item[i] == s[j]:
                    i += 1
                j += 1
            if i == len(item):
                if len(item) > len(res):
                    res = item
                if len(item) == len(res) and item < res:
                    res = item
        return res


# @lc code=end


def test():
    assert Solution().findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]) == "apple"
    assert Solution().findLongestWord("abpcplea", ["a", "b", "c"]) == "a"
    assert Solution().findLongestWord("abpcplea", ["c", "b", "a"]) == "a"
    assert Solution().findLongestWord("aewfafwafjlwajflwajflwafj", ["apple", "ewaf", "awefawfwaf", "awef", "awefe", "ewafeffewafewf"]) == "ewaf"
