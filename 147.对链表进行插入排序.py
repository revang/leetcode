#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
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
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        while head:
            pre = dummy
            while pre.next and pre.next.val < head.val:
                pre = pre.next
            nextnode = ListNode(head.val, pre.next)
            pre.next = nextnode
            head = head.next
        return dummy.next


# @lc code=end

def test():
    head = init_listnode([4, 2, 1, 3])
    print_listnode(head)
    ans = Solution().insertionSortList(head)
    print_listnode(ans)
