class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        memo = {}
        def dfs(i, j, b):
            b += 1 if grid[i][j] == '(' else -1
            if b < 0:
                return False
            if i == m - 1 and j == n - 1:
                return b == 0
            state = (i, j, b)
            if state in memo:
                return memo[state]
            res = False
            if i + 1 < m:
                res = res or dfs(i + 1, j, b)
            if j + 1 < n:
                res = res or dfs(i, j + 1, b) 
            memo[state] = res
            return res
        return dfs(0, 0, 0)
