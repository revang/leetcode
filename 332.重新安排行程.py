#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#

from typing import List
from collections import defaultdict

# @lc code=start


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        hashtable = defaultdict(list)
        for begin_address, end_address in tickets:
            hashtable[begin_address].append(end_address)
        print(hashtable)
        ans = []
# @lc code=end


def test():
    Solution().findItinerary(tickets=[["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])
