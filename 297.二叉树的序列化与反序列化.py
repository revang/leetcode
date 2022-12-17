#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

from typing import List, Optional
from collections import deque
from leetcode_tool import *


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

# @lc code=start


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        # 存储所有节点的值
        all_vals = []

        # 初始化当前层节点列表
        cur_nodes = deque()
        cur_nodes.append(root)

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
        print(",".join([",".join(cur_vals) for cur_vals in all_vals]))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
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
                if idx < len(vals) and vals[idx] is not None:  # 注意: vals[idx] is not None 不能简写成 vals[idx], 可能存在 vals[idx]==0
                    cur.left = TreeNode(vals[idx])
                    next_nodes.append(cur.left)
                idx += 1

                if idx < len(vals) and vals[idx] is not None:
                    cur.right = TreeNode(vals[idx])
                    next_nodes.append(cur.right)
                idx += 1

            cur_nodes = next_nodes

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
