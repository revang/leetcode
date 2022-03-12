#
# @lc app=leetcode.cn id=969 lang=python3
#
# [969] 煎饼排序
#

from typing import List

# @lc code=start


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)-1, 0, -1):
            max_index = arr.index(i+1)
            if max_index != i:
                ans.append(max_index+1)
                arr = list(reversed(arr[0:max_index+1]))+arr[max_index+1:]
                ans.append(i+1)
                arr = list(reversed(arr[0:i+1]))+arr[i+1:]
        return ans

# @lc code=end


def test():
    assert Solution().pancakeSort([3, 2, 4, 1]) == [3, 4, 2, 3, 1, 2]
