import heapq
class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        g = [[] for _ in range(n)]
        for i, j, w in edges:
            g[i].append((j, w))
        d = [[float('inf')] * (k + 1) for _ in range(n)]
        d[0][1] = 0
        h = [(0, 0, 1)]
        while h:
            w, i, c = heapq.heappop(h)
            if i == n - 1:
                return w
            if w > d[i][c]:
                continue
            for j, wt in g[i]:
                nc = c + 1 if labels[j] == labels[i] else 1
                if nc <= k:
                    nxt = w + wt
                    if nxt < d[j][nc]:
                        d[j][nc] = nxt
                        heapq.heappush(h, (nxt, j, nc))
        return -1
