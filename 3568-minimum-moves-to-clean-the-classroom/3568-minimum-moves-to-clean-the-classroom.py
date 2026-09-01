from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        sx, sy = -1, -1
        litters = []
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sx, sy = r, c
                elif classroom[r][c] == 'L':
                    litters.append((r, c))
        k = len(litters)
        litter_map = {pos: i for i, pos in enumerate(litters)}
        q = deque([(sx, sy, 0, energy, 0)])
        visited = {}
        while q:
            r, c, mask, e, steps = q.popleft()
            if mask == (1 << k) - 1:
                return steps
            if (r, c, mask) in visited and visited[(r, c, mask)] >= e:
                continue
            visited[(r, c, mask)] = e
            if e == 0:
                continue
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    ne = e - 1
                    nmask = mask
                    if classroom[nr][nc] == 'L' and (nr, nc) in litter_map:
                        nmask |= (1 << litter_map[(nr, nc)])
                    elif classroom[nr][nc] == 'R':
                        ne = energy
                    q.append((nr, nc, nmask, ne, steps + 1))
        return -1
