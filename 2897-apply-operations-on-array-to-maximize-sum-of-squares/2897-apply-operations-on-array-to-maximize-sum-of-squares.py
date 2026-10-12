class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        c = [0] * 30
        for x in nums:
            for i in range(30):
                if (x >> i) & 1:
                    c[i] += 1
        ans = 0
        MOD = 10**9 + 7
        for _ in range(k):
            cur = 0
            for i in range(30):
                if c[i] > 0:
                    cur |= (1 << i)
                    c[i] -= 1
            ans = (ans + cur * cur) % MOD
        return ans
