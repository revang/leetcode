#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

"""
author : revang
date   : 2022-02-02
method : 贪心-相邻问题: 先帮身高最大的找位置, 依次类推. 具体方法: 排序+插入
    1. 排序: 先按照身高从大到小排序（身高相同的情况下K小的在前面），这样的话，无论哪个人的身高都小于等于他前面人的身高。所以接下来只要按照K值将他插入相应的位置就可以了。
        例如:示例1排完序: [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]
    2. 插入: 新建一个列表
        [7,0]插入第0的位置
        [7,1]插入第1的位置
        [6,1]插入第1的位置，这时[7,1]就往后移一位了
"""

from typing import List

# @lc code=start


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people = sorted(people, key=lambda x: (-x[0], x[1]))  # x[0]降序, x1升序
        for p in people:
            res.insert(p[1], p)
        return res

# @lc code=end


def test():
    assert Solution().reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]) == [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]
