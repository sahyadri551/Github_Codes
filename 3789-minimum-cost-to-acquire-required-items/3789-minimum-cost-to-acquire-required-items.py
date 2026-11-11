class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        m = min(need1, need2)
        ans = m * min(costBoth, cost1 + cost2)
        if need1 > m:
            ans += (need1 - m) * min(cost1, costBoth)
        if need2 > m:
            ans += (need2 - m) * min(cost2, costBoth)
        return ans