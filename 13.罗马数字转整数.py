#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        hashmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s)):
            left, right = i, i+1
            if right == len(s) or hashmap[s[left]] >= hashmap[s[right]]:
                ans += hashmap[s[left]]
            else:
                ans -= hashmap[s[left]]
        return ans


# @lc code=end

def test():
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("IV") == 4
