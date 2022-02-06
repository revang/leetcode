#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
from collections import deque, defaultdict


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = defaultdict(str, {"(": ")", "[": "]", "{": "}"})
        stack = deque()
        for char in s:
            if not stack:
                if char not in pairs.keys():
                    return False
                stack.append(char)
            else:
                if char == pairs[stack[-1]]:
                    stack.pop()
                else:
                    stack.append(char)
        return len(stack) == 0

# @lc code=end


def test():
    assert Solution().isValid("()") == True
    assert Solution().isValid("()[]{}") == True
    assert Solution().isValid("(]") == False
    assert Solution().isValid(")(") == False
