class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = [['#'] * n for _ in range(m)]
        for j in range(n):
            ans[0][j] = '.'
        for i in range(m):
            ans[i][n - 1] = '.'
        return ["".join(r) for r in ans]
