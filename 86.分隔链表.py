#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
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


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        smallhead = ListNode(0)
        largehead = ListNode(0)
        small = smallhead
        large = largehead
        while head:
            if head.val < x:
                small.next = ListNode(head.val)
                small = small.next
                head = head.next
            else:
                large.next = ListNode(head.val)
                large = large.next
                head = head.next
        small.next = largehead.next
        return smallhead.next


# @lc code=end

def test():
    head = init_listnode([1, 4, 3, 2, 5, 2])
    print_listnode(head)
    ans = Solution().partition(head, 3)
    print_listnode(ans)
