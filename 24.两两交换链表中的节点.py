#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
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
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(None, head)
        pre = dummy  # pre 为需要交换节点的前一个节点
        while pre.next and pre.next.next:
            fst = pre.next
            sec = fst.next
            thr = sec.next
            pre.next = sec
            sec.next = fst
            fst.next = thr
            pre = pre.next.next
        return dummy.next


# @lc code=end


def test():
    head = init_listnode([1, 2, 3, 4])
    print_listnode(head)
    ans = Solution().swapPairs(head)
    print_listnode(ans)
