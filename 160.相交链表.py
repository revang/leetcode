#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1


# @lc code=end

def test():
    common = ListNode(8, ListNode(4, ListNode(5)))
    listA = ListNode(4, ListNode(1, common))
    listB = ListNode(5, ListNode(6, ListNode(1, common)))
    ans = Solution().getIntersectionNode(listA, listB)
    print_listnode(ans)
