#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        isprime = [True]*(n)
        for i in range(2, int(n**0.5)+1):
            if isprime[i]:
                for j in range(i*i, n, i):
                    isprime[j] = False
        return len([x for x in range(2, n) if isprime[x]])


# @lc code=end

def test():
    assert Solution().countPrimes(10) == 4
    assert Solution().countPrimes(3) == 1
    assert Solution().countPrimes(2) == 0
