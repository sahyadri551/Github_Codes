class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                for d in range(1, length):
                    if length % d == 0:
                        cur_cost = 0
                        for group in range(d):
                            l = i + group
                            r = i + length - (d - group)
                            while l < r:
                                if s[l] != s[r]:
                                    cur_cost += 1
                                l += d
                                r -= d
                        cost[i][j] = min(cost[i][j], cur_cost)
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for i in range(1, n + 1):
            for p in range(1, min(k, i) + 1):
                for j in range(i - 1):
                    dp[i][p] = min(dp[i][p], dp[j][p - 1] + cost[j][i - 1])
                    
        return dp[n][k]
