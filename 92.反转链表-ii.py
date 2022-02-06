#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
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
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0, head)
        pretail = dummy
        for _ in range(left-1):
            pretail = pretail.next

        midhead, midtail = pretail.next, pretail.next
        for _ in range(right-left):
            midtail = midtail.next

        posthead = midtail.next

        midtail.next = None
        pretail.next = None
        midhead = self.reverse_listnode(midhead)
        midtail = midhead
        for _ in range(right-left):
            midtail = midtail.next

        midtail.next = posthead
        pretail.next = midhead
        return dummy.next

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
    print("testcase 1")
    head = init_listnode([1, 2, 3, 4, 5])
    print_listnode(head)
    ans = Solution().reverseBetween(head, 2, 4)
    print_listnode(ans)

    print("testcase 2")
    head = init_listnode([5])
    print_listnode(head)
    ans = Solution().reverseBetween(head, 1, 1)
    print_listnode(ans)

    print("testcase 3")
    head = init_listnode([3, 5])
    print_listnode(head)
    ans = Solution().reverseBetween(head, 1, 2)
    print_listnode(ans)
