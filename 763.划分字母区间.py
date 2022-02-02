#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

"""
author : revang
date   : 2022-02-02
method : 贪心-区间问题
    1. 在处理数组前，统计一遍信息（每个字符开始位置，结束位置）
    2. 转换位贪婪-区间问题
"""

from typing import List

# @lc code=start


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashtable = {}
        for idx, val in enumerate(s):
            if val not in hashtable:
                hashtable[val] = [idx, idx]
            else:
                hashtable[val] = [hashtable[val][0], idx]
        interval_list = hashtable.values()
        interval_list = sorted(interval_list, key=lambda x: x[0])
        ans, pre_start, pre_end, size = [],  0, interval_list[0][1], len(interval_list)
        print(interval_list)
        for i in range(1, size):
            if interval_list[i][0] >= pre_end:
                ans.append(pre_end-pre_start+1)
                pre_start = interval_list[i][0]
            pre_end = max(pre_end, interval_list[i][1])
        ans.append(pre_end-pre_start+1)
        return ans
# @lc code=end


def test():
    assert Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert Solution().findMinArrowShots([[1, 2]]) == 1
    assert Solution().findMinArrowShots([[2, 3], [2, 3]]) == 1
