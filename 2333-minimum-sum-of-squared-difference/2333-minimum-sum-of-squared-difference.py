class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        mx = max(diff) if diff else 0
        if mx == 0:
            return 0
        cnt = [0] * (mx + 1)
        for d in diff:
            cnt[d] += 1
        for d in range(mx, 0, -1):
            if cnt[d] > 0:
                t = min(k, cnt[d])
                cnt[d] -= t
                cnt[d - 1] += t
                k -= t
                if k == 0:
                    break
        return sum(d * d * cnt[d] for d in range(1, mx + 1))
