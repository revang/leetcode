#
# @lc app=leetcode.cn id=1290 lang=python3
#
# [1290] 二进制链表转整数
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
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        cur = head
        while cur:
            ans = ans*2+cur.val
            cur = cur.next
        return ans

# @lc code=end


def test():
    head = init_listnode([1, 0, 1])
    assert Solution().getDecimalValue(head) == 5
