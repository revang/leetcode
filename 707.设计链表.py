#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#


def print_listnode(head):
    """ 打印单链表 """
    cur = head
    while cur:
        print("{}->".format(cur.val), end="")
        cur = cur.next
    print("None")

# @lc code=start


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val, self.prev, self.next = val, prev, next


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.headdummy, self.taildummy = ListNode(0), ListNode(0)
        self.headdummy.next = self.taildummy
        self.taildummy.prev = self.headdummy

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.headdummy
        for _ in range(index+1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        prevnode = self.headdummy
        nextnode = self.headdummy.next
        node.prev = prevnode
        node.next = nextnode
        prevnode.next = node
        nextnode.prev = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        prevnode = self.taildummy.prev
        nextnode = self.taildummy
        node.prev = prevnode
        node.next = nextnode
        prevnode.next = node
        nextnode.prev = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif 0 < index < self.size:
            curr = self.headdummy
            for _ in range(index+1):
                curr = curr.next
            node = ListNode(val)
            prevnode = curr.prev
            nextnode = curr
            node.prev = prevnode
            node.next = nextnode
            prevnode.next = node
            nextnode.prev = node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.headdummy
        for _ in range(index+1):
            curr = curr.next
        prevnode = curr.prev
        nextnode = curr.next
        prevnode.next = nextnode
        nextnode.prev = prevnode
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:

# @lc code=end

def test():
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)
    assert linkedList.get(1) == 2
    linkedList.deleteAtIndex(1)
    print_listnode(linkedList.headdummy)
    assert linkedList.get(1) == 3
    print_listnode(linkedList.headdummy)
