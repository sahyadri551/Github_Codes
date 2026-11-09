class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        n = 1
        while n < k:
            n *= 2
        tree = [0] * (2 * n)
        for i in range(k):
            tree[n + i] = 1
        for i in range(n - 1, 0, -1):
            tree[i] = tree[2 * i] | tree[2 * i + 1]
        def update(idx, val):
            idx += n
            tree[idx] = val
            idx //= 2
            while idx > 0:
                tree[idx] = tree[2 * idx] | tree[2 * idx + 1]
                idx //= 2
        def query(node, l, r, ql, qr):
            if l >= qr or r <= ql or not tree[node]:
                return -1
            if l == r - 1:
                return l
            mid = (l + r) // 2
            res = query(2 * node, l, mid, ql, qr)
            if res != -1:
                return res
            return query(2 * node + 1, mid, r, ql, qr)
        h = []
        def push(time, s_id):
            h.append((time, s_id))
            curr = len(h) - 1
            while curr > 0:
                p = (curr - 1) // 2
                if h[curr] < h[p]:
                    h[curr], h[p] = h[p], h[curr]
                    curr = p
                else:
                    break
        def pop():
            res = h[0]
            last = h.pop()
            if h:
                h[0] = last
                curr = 0
                while 2 * curr + 1 < len(h):
                    left = 2 * curr + 1
                    right = left + 1
                    small = left
                    if right < len(h) and h[right] < h[left]:
                        small = right
                    if h[small] < h[curr]:
                        h[curr], h[small] = h[small], h[curr]
                        curr = small
                    else:
                        break
            return res
        cnt = [0] * k
        for i, t in enumerate(arrival):
            while h and h[0][0] <= t:
                _, s_id = pop()
                update(s_id, 1)
            target = i % k
            idx = query(1, 0, n, target, k)
            if idx == -1:
                idx = query(1, 0, n, 0, target)
            if idx != -1:
                cnt[idx] += 1
                update(idx, 0)
                push(t + load[i], idx)
        mx = max(cnt)
        return [i for i, c in enumerate(cnt) if c == mx]
