class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        tree = [[0, 0] for _ in range(4 * n)]
        lazy = [0] * (4 * n)
        def upd(i, l, r, ql, qr):
            if ql <= l and r <= qr:
                tree[i][1] = (tree[i][1] + 2 * tree[i][0] + (r - l + 1)) % MOD
                tree[i][0] = (tree[i][0] + (r - l + 1)) % MOD
                lazy[i] += 1
                return
            if lazy[i]:
                m, v = (l + r) // 2, lazy[i]
                for ch, sz in ((2*i, m - l + 1), (2*i + 1, r - m)):
                    lazy[ch] += v
                    tree[ch][1] = (tree[ch][1] + 2 * v * tree[ch][0] + v * v * sz) % MOD
                    tree[ch][0] = (tree[ch][0] + v * sz) % MOD
                lazy[i] = 0
            m = (l + r) // 2
            if ql <= m: upd(2*i, l, m, ql, qr)
            if qr > m: upd(2*i+1, m+1, r, ql, qr)
            tree[i][0] = (tree[2*i][0] + tree[2*i+1][0]) % MOD
            tree[i][1] = (tree[2*i][1] + tree[2*i+1][1]) % MOD
        ans, last = 0, {}
        for i, x in enumerate(nums):
            upd(1, 0, n - 1, last.get(x, -1) + 1, i)
            ans = (ans + tree[1][1]) % MOD
            last[x] = i  
        return ans
