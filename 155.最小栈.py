#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
from collections import deque


class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0


class MinStack:
    def __init__(self):
        self.s = Stack()
        self.smin = Stack()

    def push(self, val: int) -> None:
        if self.smin.empty():
            minval = val
        elif val < self.smin.top():
            minval = val
        else:
            minval = self.smin.top()
        self.s.push(val)
        self.smin.push(minval)

    def pop(self) -> None:
        self.smin.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s.top()

    def getMin(self) -> int:
        return self.smin.top()


# @lc code=end
def test():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    assert minStack.pop() == -3
    assert minStack.top() == 0
    assert minStack.getMin() == -2
