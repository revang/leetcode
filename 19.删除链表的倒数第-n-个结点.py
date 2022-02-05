#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def init_listnode(nums):
    """ 列表生成单链表 """
    if not nums:
        return
    dummy = ListNode(None)
    cur = dummy
    for i in range(len(nums)):
        next = ListNode(nums[i])
        cur.next = next
        cur = cur.next
    return dummy.next


def print_listnode(head):
    """ 打印单链表 """
    cur = head
    while cur:
        print("{}->".format(cur.val), end="")
        cur = cur.next
    print("None")


# @lc code=start

# 先求出长度再删除
# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         dummy = ListNode(None, head)
#         cur = dummy
#         size = self.listnode_length(head)
#         for _ in range(size-n):
#             cur = cur.next
#         cur.next = cur.next.next
#         return dummy.next

#     def listnode_length(self, head):
#         length = 0
#         while head:
#             length += 1
#             head = head.next
#         return length

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        slow, fast = dummy, head
        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

# @lc code=end


def test():
    print("demo 1")
    head = init_listnode([1, 2, 3, 4, 5])
    print_listnode(head)
    ans = Solution().removeNthFromEnd(head, 2)
    # print_listnode(head)  # 虽然调用了listnode_length, 但是listnode没有改变
    print_listnode(ans)

    # print("demo 2")
    # head = init_listnode([1])
    # print_listnode(head)
    # ans = Solution().removeNthFromEnd(head, 1)
    # print_listnode(ans)
