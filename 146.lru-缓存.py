#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
# from collections import OrderedDict


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.od = OrderedDict()  # 底层是循环双端链表实现的
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self.od:
#             return -1
#         self.od.move_to_end(key)
#         return self.od[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.od:
#             self.od[key] = value
#         else:
#             self.od[key] = value
#             if len(self.od) > self.capacity:
#                 self.od.popitem(last=False)
#         self.od.move_to_end(key)

from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict()
        self.dq = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.dq.remove(key)
        self.dq.append(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key] = value
        else:
            self.dic[key] = value
            self.dq.append(key)
            if len(self.dic) > self.capacity:
                remove_key = self.dq.popleft()
                self.dic.pop(remove_key)
        self.dq.remove(key)
        self.dq.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# @lc code=end


def test():
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    assert lRUCache.get(1) == 1
    lRUCache.put(3, 3)
    assert lRUCache.get(2) == -1
    lRUCache.put(4, 4)
    assert lRUCache.get(1) == -1
    assert lRUCache.get(3) == 3
    assert lRUCache.get(4) == 4
