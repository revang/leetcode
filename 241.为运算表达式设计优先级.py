#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

from typing import List

# @lc code=start


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():  # 如果只有数字, 直接返回
            return [int(expression)]

        ans = []
        for idx, char in enumerate(expression):
            if char in ("+", "-", "*"):
                # 1. 分: 遇到运算符, 计算左右两侧结果
                # 2. 治: diffWaysToCompute递归函数求出子问题的解
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx+1:])
                for l in left:
                    for r in right:
                        if char == "+":
                            ans.append(l+r)
                        elif char == "-":
                            ans.append(l-r)
                        else:
                            ans.append(l*r)
        return ans


# @lc code=end


def test():
    assert sorted(Solution().diffWaysToCompute("2-1-1")) == [0, 2]
    assert sorted(Solution().diffWaysToCompute("2*3-4*5")) == [-34, -14, -10, -10, 10]
