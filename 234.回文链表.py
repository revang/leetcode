#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
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
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = self.reverse_listnode(slow.next)
        slow = slow.next
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True

    def reverse_listnode(self, head):
        pre = None
        cur = head
        while cur:
            nextnode = cur.next
            cur.next = pre
            pre = cur
            cur = nextnode
        return pre

# @lc code=end


def test():
    head = init_listnode([1, 2, 2, 1])
    print_listnode(head)
    assert Solution().isPalindrome(head) == True

    head = init_listnode([1, 2])
    print_listnode(head)
    assert Solution().isPalindrome(head) == False
