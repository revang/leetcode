#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

from collections import defaultdict
# @lc code=start


class Solution:  # HashTable
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap = {key: 0 for key in jewels}
        cnt = sum([1 for i in stones if i in hashmap])
        return cnt
# @lc code=end


def test():
    assert Solution().numJewelsInStones("aA", "aAAbbbb") == 3
    assert Solution().numJewelsInStones("z", "ZZ") == 0
