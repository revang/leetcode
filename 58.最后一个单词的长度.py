#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = len(s)-1
        while right >= 0:
            if s[right] != " ":
                break
            right -= 1
        if right < 0:
            return 0

        left = right-1
        while left >= 0:
            if s[left] == " ":
                break
            left -= 1
        return right-left


# @lc code=end
def test():
    assert Solution().lengthOfLastWord("Hello World") == 5
    assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert Solution().lengthOfLastWord("cat") == 3
    assert Solution().lengthOfLastWord("") == 0
    assert Solution().lengthOfLastWord(" ") == 0
