#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        common_prefix = ""
        while i < len(strs):
            if len(strs) == 1:
                common_prefix = strs[i]
                break
            if i == 0:
                common_prefix = self.CommonPrefix(strs[0], strs[1])
            else:
                common_prefix = self.CommonPrefix(common_prefix, strs[i])
            i += 1
        return common_prefix

    def CommonPrefix(self, str1, str2) -> str:
        i = 0
        while i < len(str1) and i < len(str2):
            if str1[i] != str2[i]:
                break
            i += 1
        return str1[:i]

# @lc code=end


def test():
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
