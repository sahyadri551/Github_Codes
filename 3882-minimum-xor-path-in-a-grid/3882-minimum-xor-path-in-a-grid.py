class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dp = [set() for _ in range(C)]
        dp[0].add(grid[0][0])
        for j in range(1, C):
            for x in dp[j - 1]:
                dp[j].add(x ^ grid[0][j])
        for i in range(1, R):
            nxt = [set() for _ in range(C)]
            for j in range(C):
                for x in dp[j]:
                    nxt[j].add(x ^ grid[i][j])
                if j > 0:
                    for x in nxt[j - 1]:
                        nxt[j].add(x ^ grid[i][j])
            dp = nxt
        return min(dp[-1])
