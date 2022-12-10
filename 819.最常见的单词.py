#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

from typing import List

# @lc code=start

from collections import defaultdict


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        hashmap = defaultdict(int)
        paragraph = paragraph.lower()
        paragraph = paragraph.replace("!", " ").replace("?", " ").replace("'", " ").replace(",", " ").replace(";", " ").replace(".", " ")
        word_list = paragraph.split(" ")
        for word in word_list:
            if word not in banned and len(word) > 0:
                hashmap[word] += 1
        return max(hashmap, key=hashmap.get)


# @lc code=end
def test():
    assert Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]) == "ball"
    assert Solution().mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]) == "ball"
