class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        for v in nums:
            nxt = [0] * k
            r = v % k
            nxt[r] += 1
            for j in range(k):
                if dp[j] > 0:
                    nxt[(j * r) % k] += dp[j]
            for j in range(k):
                dp[j] = nxt[j]
                ans[j] += dp[j]
        return ans
