from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Tree:
    def __init__(self, vals=[]):
        self.root = None
        self.create(vals)

    def create(self, vals):
        """
        创建树
        """
        if len(vals) == 0:
            return

        # 创建根节点
        root = TreeNode(vals[0])
        cur_nodes = deque()
        cur_nodes.append(root)
        idx = 1

        # 遍历值列表，并逐个创建节点
        while cur_nodes:
            next_nodes = deque()
            while cur_nodes:
                cur = cur_nodes.popleft()
                if idx < len(vals) and vals[idx]:
                    cur.left = TreeNode(vals[idx])
                    next_nodes.append(cur.left)
                idx += 1

                if idx < len(vals) and vals[idx]:
                    cur.right = TreeNode(vals[idx])
                    next_nodes.append(cur.right)
                idx += 1

            cur_nodes = next_nodes

        self.root = root

    def print(self):
        """
        打印树
        """
        if not self.root:
            print()

        # 存储所有节点的值
        all_vals = []

        # 初始化当前层节点列表
        cur_nodes = deque()
        cur_nodes.append(self.root)

        # 遍历所有层
        while any(cur_nodes):
            # 存储当前层节点的值
            cur_vals = [str(item.val) if item else "None" for item in cur_nodes]
            all_vals.append(cur_vals)

            # 遍历当前层的所有节点
            next_nodes = deque()
            while cur_nodes:
                cur = cur_nodes.popleft()
                next_nodes.append(cur.left if cur and cur.left else None)
                next_nodes.append(cur.right if cur and cur.right else None)

            # 更新当前层节点列表
            cur_nodes = next_nodes

        # 打印所有节点的值
        print("; ".join([", ".join(cur_vals) for cur_vals in all_vals]))


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """
    如何判断两棵树是否相同
    """
    # 如果两棵树都是空树，那么它们相同
    if not p and not q:
        return True

    # 如果只有一棵树是空树，那么它们不相同
    if not p or not q:
        return False

    # 如果两棵树的根节点值不相同，那么它们不相同
    if p.val != q.val:
        return False

    # 如果两棵树的左子树不相同或右子树不相同，那么它们不相同
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
