#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2:
            sum = carry+(l1.val if l1 else 0)+(l2.val if l2 else 0)
            carry = sum//10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry == 1:
            cur.next = ListNode(carry)
        return dummy.next

# @lc code=end


def test():
    print("demo 1:")
    l1 = init_listnode([2, 4, 3])
    l2 = init_listnode([5, 6, 4])
    print_listnode(l1)
    print_listnode(l2)
    ans = Solution().addTwoNumbers(l1, l2)
    print_listnode(ans)

    print("demo 2:")
    l1 = init_listnode([9, 9, 9, 9, 9, 9, 9])
    l2 = init_listnode([9, 9, 9, 9])
    print_listnode(l1)
    print_listnode(l2)
    ans = Solution().addTwoNumbers(l1, l2)
    print_listnode(ans)
