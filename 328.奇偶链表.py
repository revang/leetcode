#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
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
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        evenhead = head.next
        odd, even = head, head.next  # odd 奇数, even 偶数
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenhead
        return head

# @lc code=end


def test():
    print("demo 1")
    head = init_listnode([1, 2, 3, 4, 5])
    print_listnode(head)
    ans = Solution().oddEvenList(head)
    print_listnode(ans)

    print("demo 2")
    head = init_listnode([2, 1, 3, 5, 6, 4, 7])
    print_listnode(head)
    ans = Solution().oddEvenList(head)
    print_listnode(ans)
