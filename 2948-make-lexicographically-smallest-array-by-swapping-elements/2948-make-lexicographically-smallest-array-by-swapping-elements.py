from collections import deque
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        s = sorted(nums)
        g = []
        m = {}
        for v in s:
            if not g or v - g[-1][-1] > limit:
                g.append(deque())
            g[-1].append(v)
            m[v] = len(g) - 1
        res = []
        for v in nums:
            res.append(g[m[v]].popleft())
        return res
