from collections import Counter
from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        m = len(queries)
        qs = sorted(range(m), key=lambda i: queries[i])
        logs.sort(key=lambda t: t[1])
        ans = [0] * m
        cnt = Counter()
        j = 0
        k = 0
        l = len(logs)
        for i in qs:
            t = queries[i]
            while k < l and logs[k][1] <= t:
                cnt[logs[k][0]] += 1
                k += 1
            while j < l and logs[j][1] < t - x:
                cnt[logs[j][0]] -= 1
                if cnt[logs[j][0]] == 0:
                    del cnt[logs[j][0]]
                j += 1
            ans[i] = n - len(cnt)
        return ans
