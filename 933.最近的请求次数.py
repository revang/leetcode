#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#

from collections import deque

# @lc code=start


class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

def test():
    recentCounter = RecentCounter()
    assert recentCounter.ping(1) == 1     # requests = [1]，范围是 [-2999,1]，返回 1
    assert recentCounter.ping(100) == 2   # requests = [1, 100]，范围是 [-2900,100]，返回 2
    assert recentCounter.ping(3001) == 3  # requests = [1, 100, 3001]，范围是 [1,3001]，返回 3
    assert recentCounter.ping(3002) == 3  # requests = [1, 100, 3001, 3002]，范围是 [2,3002]，返回 3
