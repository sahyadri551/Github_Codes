class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rc = [0] * m
        cc = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rc[i] += 1
                    cc[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (rc[i] > 1 or cc[j] > 1):
                    ans += 1
        return ans
