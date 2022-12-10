#
# @lc app=leetcode.cn id=2124 lang=python3
#
# [2124] 检查是否所有 A 都在 B 之前
#

# @lc code=start
# class Solution:
#     def checkString(self, s: str) -> bool:
#         """
#         双指针
#         a从右边开始移动, 移动到第一个a字母停止, 如果a不存在则返回True
#         b从左边开始移动, 移动到a指针位置停止, 如果在这之前找到了b字母返回False, 否则返回True
#         """
#         right = len(s)-1
#         while right >= 0:
#             if s[right] == "a":
#                 break
#             right -= 1
#         if right == -1:
#             return True

#         left = 0
#         while left < right:
#             if s[left] == "b":
#                 break
#             left += 1
#         print(left, right, 1000)
#         if left == right:
#             return True
#         if left < right:
#             return False

class Solution:
    def checkString(self, s: str) -> bool:
        return s.find("ba") < 0
# @lc code=end


def test():
    assert Solution().checkString("aaabbb") == True
    assert Solution().checkString("abab") == False
    assert Solution().checkString("bbb") == True
