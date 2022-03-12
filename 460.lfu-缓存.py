#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU 缓存
#

# dict+双链表

# @lc code=start
from collections import defaultdict
import collections


class Node:
    def __init__(self, key, val, prev=None, next=None, freq=0):
        self.key, self.val, self.prev, self.next, self.freq = key, val, prev, next, freq

    def insert(self, key, val):
        node = Node(key, val)
        prevnode = self.next
        node.prev = prevnode
        prevnode.next = node


def create_linked_list():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.next = tail
    tail.prev = head
    return (head, tail)


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.freqMap = collections.defaultdict(create_linked_list)
        self.keyMap = {}

    def delete(self, node):
        if node.prev:
            prevnode = node.prev
            nextnode = node.next
            prevnode.next = nextnode
            nextnode.prev = prevnode

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1

        # self.lst.remove(key)
        # self.lst.append(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.dic[key] = value
            self.lst.remove(key)
            self.lst.append(key)
        else:
            self.dic[key] = value
            self.lst.append(key)
            if len(self.dic) > self.capacity:
                remove_key = self.dq.popleft()
                self.dic.pop(remove_key)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

def test():
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    assert lfu.get(1) == 1
    lfu.put(3, 3)
    assert lfu.get(2) == -1
    assert lfu.get(3) == 3
    lfu.put(4, 4)
    assert lfu.get(1) == -1
    assert lfu.get(3) == 3
    assert lfu.get(4) == 4
