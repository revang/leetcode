#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        pre = dummy
        while pre.next and pre.next.next:
            if pre.next.val == pre.next.next.val:
                x = pre.next.val
                while pre.next and pre.next.val == x:
                    pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy.next

# @lc code=end


def test():
    print("demo 1:")
    head = init_listnode([1, 2, 3, 3, 4, 4, 5])
    print_listnode(head)
    ans = Solution().deleteDuplicates(head)
    print_listnode(ans)

    print("demo 2:")
    head = init_listnode([1, 1, 1, 2, 3])
    print_listnode(head)
    ans = Solution().deleteDuplicates(head)
    print_listnode(ans)
