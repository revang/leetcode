#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

"""
author : revang
date   : 2022-02-01
method : 双指针
    1. 如果字符串是回文字符串: 返回True
    2. 如果字符串不是回文字符串: 判断 [左指针+1,右指针](闭区间) 和 [左指针,右指针+1](闭区间) 的字符串是否是回文字符串, 只要有一个是结果就是True
"""


# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(chars):
            left, right = 0, len(chars)-1
            while left < right:
                if chars[left] != chars[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
            left += 1
            right -= 1
        return True


# @lc code=end

def test():
    assert Solution().validPalindrome("aba") == True
    assert Solution().validPalindrome("abca") == True
    assert Solution().validPalindrome("abc") == False
    assert Solution().validPalindrome("deeee") == True
