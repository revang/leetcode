#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

import heapq
from typing import List
from collections import defaultdict

# @lc code=start


# 桶排序(哈希表)
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         hashtable = defaultdict(int)
#         for num in nums:
#             hashtable[num] += 1
#         sorted_list = sorted(hashtable.items(), key=lambda x: x[1], reverse=True)
#         idx = 0
#         res = []
#         while idx < k:
#             res.append(sorted_list[idx][0])
#             idx += 1
#         return res

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, key, val):
        self.heap.append((key, val))
        self.size += 1
        idx = self.size-1
        parent_idx = (idx-1)//2
        while self.heap[idx][0] < self.heap[parent_idx][0] and idx > 0:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
            parent_idx = (idx-1)//2
        print(self.heap)

    def peek(self):
        return self.heap[0]

    def pop(self):
        if self.size == 1:
            self.size -= 1
            return self.heap.pop()
        ans = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.size -= 1
        idx = 0
        while idx*2+2 < self.size:
            left, right = idx*2+1, idx*2+2
            if self.heap[left][0] < self.heap[idx][0]:
                self.heap[idx], self.heap[left] = self.heap[left], self.heap[idx]
                idx = left
            elif self.heap[right][0] < self.heap[idx][0]:
                self.heap[idx], self.heap[right] = self.heap[right], self.heap[idx]
                idx = right
            else:
                break
        return ans

    def size(self):
        return self.size

    def __repr__(self):
        return str(self.heap)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = defaultdict(int)
        for num in nums:
            hashtable[num] += 1

        heap = MinHeap()
        for key, val in hashtable.items():
            if heap.size < k:
                heap.push(val, key)
            else:
                if val > int(heap.peek()[0]):
                    heap.pop()
                    heap.push(val, key)
        print(heap.heap)

        ans = []
        while heap.size > 0:
            item = heap.pop()
            ans.append(item[1])
        return ans

# @lc code=end


def test():
    assert Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2) == [2, 1]
    assert Solution().topKFrequent([1], 1) == [1]
    assert Solution().topKFrequent([5, -3, 9, 1, 7, 7, 9, 10, 2, 2, 10, 10, 3, -1, 3, 7, -9, -1, 3, 3], 3) == [3, 7, 10]
