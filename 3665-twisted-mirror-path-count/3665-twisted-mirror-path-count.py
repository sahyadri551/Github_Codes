class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        memo = {}
        def move(r, c, d):
            if (r, c, d) in memo:
                return memo[(r, c, d)]
            curr_r, curr_c, curr_d = r, c, d
            while 0 <= curr_r < m and 0 <= curr_c < n:
                if grid[curr_r][curr_c] == 0:
                    memo[(r, c, d)] = (curr_r, curr_c)
                    return memo[(r, c, d)]
                if curr_d == 0:
                    curr_r += 1
                    curr_d = 1
                else:
                    curr_c += 1
                    curr_d = 0
            memo[(r, c, d)] = None
            return None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 or dp[i][j] == 0:
                    continue
                nxt_r = move(i, j + 1, 0)
                if nxt_r:
                    ni, nj = nxt_r
                    dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD
                nxt_d = move(i + 1, j, 1)
                if nxt_d:
                    ni, nj = nxt_d
                    dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % MOD
        return dp[m - 1][n - 1]
