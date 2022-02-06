#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
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


class MyQueue:

    def __init__(self):
        self.s1 = Stack()  # 栈1: 入栈
        self.s2 = Stack()  # 栈2: 出栈

    def push(self, x: int) -> None:
        self.move_to_s1()
        self.s1.push(x)

    def pop(self) -> int:
        self.move_to_s2()
        return self.s2.pop()

    def peek(self) -> int:
        self.move_to_s2()
        return self.s2.top()

    def empty(self) -> bool:
        return self.s1.empty() and self.s2.empty()

    def move_to_s1(self):
        """ 移动栈2元素到栈1. 注意: 移动前栈1必须是空的 """
        while not self.s2.empty():
            self.s1.push(self.s2.pop())

    def move_to_s2(self):
        """ 移动栈1元素到栈2. 注意: 移动前栈2必须是空的 """
        while not self.s1.empty():
            self.s2.push(self.s1.pop())

# @lc code=end


def test():
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    print(myQueue.peek())
    print(myQueue.pop())
    print(myQueue.empty())
