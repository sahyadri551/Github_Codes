class Solution:

    def closedIsland(self, grid: list[list[int]]) -> int:
        R, C = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 1:
                return
            grid[r][c] = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(R):
            dfs(r, 0)
            dfs(r, C - 1)
        for c in range(C):
            dfs(0, c)
            dfs(R - 1, c)
        ans = 0
        for r in range(1, R - 1):
            for c in range(1, C - 1):
                if grid[r][c] == 0:
                    dfs(r, c)
                    ans += 1
        return ans
