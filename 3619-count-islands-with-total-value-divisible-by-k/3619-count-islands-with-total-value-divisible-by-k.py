class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] > 0:
                    s = 0
                    q = [(r, c)]
                    grid[r][c] = -grid[r][c]
                    while q:
                        i, j = q.pop()
                        s -= grid[i][j]
                        for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                            if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] > 0:
                                grid[ni][nj] = -grid[ni][nj]
                                q.append((ni, nj))
                    if s % k == 0:
                        ans += 1                
        return ans