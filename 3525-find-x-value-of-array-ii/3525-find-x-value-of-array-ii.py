class Solution:
    def resultArray(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[int]:
        n = len(nums)
        t = [[0] * k for _ in range(4 * n)]
        p = [1] * (4 * n)
        def b(o, l, r):
            if l == r:
                v = nums[l] % k
                t[o][v] = 1
                p[o] = v
                return
            m = (l + r) // 2
            b(2 * o, l, m)
            b(2 * o + 1, m + 1, r)
            p[o] = (p[2 * o] * p[2 * o + 1]) % k
            for i in range(k):
                t[o][i] = t[2 * o][i]
            for i in range(k):
                t[o][(p[2 * o] * i) % k] += t[2 * o + 1][i]
        def u(o, l, r, idx, v):
            if l == r:
                t[o] = [0] * k
                t[o][v] = 1
                p[o] = v
                return
            m = (l + r) // 2
            if idx <= m:
                u(2 * o, l, m, idx, v)
            else:
                u(2 * o + 1, m + 1, r, idx, v)
            p[o] = (p[2 * o] * p[2 * o + 1]) % k
            for i in range(k):
                t[o][i] = t[2 * o][i]
            for i in range(k):
                t[o][(p[2 * o] * i) % k] += t[2 * o + 1][i]
        def q(o, l, r, ql, qr):
            if ql <= l and r <= qr:
                return t[o], p[o]
            m = (l + r) // 2
            if qr <= m:
                return q(2 * o, l, m, ql, qr)
            if ql > m:
                return q(2 * o + 1, m + 1, r, ql, qr)
            lt, lp = q(2 * o, l, m, ql, qr)
            rt, rp = q(2 * o + 1, m + 1, r, ql, qr)
            ct = [0] * k
            for i in range(k):
                ct[i] = lt[i]
            for i in range(k):
                ct[(lp * i) % k] += rt[i]
            return ct, (lp * rp) % k
        b(1, 0, n - 1)
        ans = []
        for idx, val, start, x in queries:
            u(1, 0, n - 1, idx, val % k)
            res_t, _ = q(1, 0, n - 1, start, n - 1)
            ans.append(res_t[x])
        return ans
