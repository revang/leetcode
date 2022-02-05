#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
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


# 递归(实现1)
# class Solution:
#     def reverseList(self, head: ListNode, pre=None) -> ListNode:
#         if not head:
#             return pre
#         next = head.next
#         head.next = pre
#         return self.reverseList(next, head)

# 递归(实现2)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newhead = self.reverseList(head.next)
        nextnode = head.next
        nextnode.next = head
        head.next = None
        return newhead

# 非递归
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         pre = None
#         cur = head
#         while cur:
#             nextnode = cur.next
#             cur.next = pre
#             pre = cur
#             cur = nextnode
#         return pre


# @lc code=end


def test():
    head = init_listnode([1, 2, 3, 4, 5])
    print_listnode(head)
    ans = Solution().reverseList(head)
    print_listnode(ans)
