#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#


from typing import List

# @lc code=start

# 快速选择(快速排序)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         if not nums:
#             return
#         if len(nums) == 1:  # 递归出口
#             return nums[0]
#         pivot, pivot_idx, size = nums[0], 0, len(nums)  # pivot 基准
#         less_part = [nums[i] for i in range(size) if nums[i] <= pivot and pivot_idx != i]  # 小于等于基准值的子数组. less 更少的
#         great_part = [nums[i] for i in range(size) if nums[i] > pivot and pivot_idx != i]  # 大于基准值的子数组. great 更多的
#         if len(great_part)+1 == k:
#             return pivot
#         elif len(great_part)+1 > k:  # 在右边
#             return self.findKthLargest(great_part, k)
#         else:  # 在左边
#             return self.findKthLargest(less_part, k-len(great_part)-1)


from heapq import heappop, heapify, heappush


# class Solution:  # The Kth问题-解法1
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = [-num for num in nums]
#         heapify(heap)
#         for _ in range(k-1):
#             heappop(heap)
#         return -heappop(heap)


class Solution:  # The Kth问题-解法2
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) < k:
                heappush(heap, num)
            else:
                if num >= heap[0]:
                    heappop(heap)
                    heappush(heap, num)
        return heap[0]


# @lc code=end


def test():
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert Solution().findKthLargest([1], 1) == 1
    assert Solution().findKthLargest([2, 1], 2) == 1
    assert Solution().findKthLargest([-1, -1], 2) == -1
