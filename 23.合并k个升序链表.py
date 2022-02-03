#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

from multiprocessing import dummy
from typing import List
from heapq import heapify, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        for node in lists:
            while node:
                h.append(node.val)
                node = node.next
        heapify(h)  # 构造一个最小堆
        dummy = ListNode(None)
        cur = dummy
        while h:
            nextnode = ListNode(heappop(h))
            cur.next = nextnode
            cur = cur.next
        return dummy.next
        # @lc code=end
