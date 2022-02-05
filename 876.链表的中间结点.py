#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
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
    def middleNode(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            slow = slow.next
        return slow


# @lc code=end
def test():
    head = init_listnode([1, 2, 3, 4, 5])
    print_listnode(head)
    ans = Solution().middleNode(head)
    print_listnode(ans)

    head = init_listnode([1, 2, 3, 4, 5, 6])
    print_listnode(head)
    ans = Solution().middleNode(head)
    print_listnode(ans)
