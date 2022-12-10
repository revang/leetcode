#
# @lc app=leetcode.cn id=2129 lang=python3
#
# [2129] 将标题首字母大写
#

# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        word_list = title.lower().split(" ")
        for i in range(len(word_list)):
            word = word_list[i]
            if len(word) >= 3:
                word = word[0].upper()+word[1:]
            word_list[i] = word
        return " ".join(word_list)

# @lc code=end


def test():
    assert Solution().capitalizeTitle("capiTalIze tHe titLe") == "Capitalize The Title"
    assert Solution().capitalizeTitle("First leTTeR of EACH Word") == "First Letter of Each Word"
    assert Solution().capitalizeTitle("i lOve leetcode") == "i Love Leetcode"
