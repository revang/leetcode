#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

from typing import List
# @lc code=start


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            val = bin(i)
            count = len(val)-len(val.replace("1", ""))
            ans.append(count)
        return ans

# @lc code=end


def test():
    assert Solution().countBits(2) == [0, 1, 1]
