class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        dp = [float('inf')] * n
        res = float('inf')
        cur = 0
        l = 0
        min_l = float('inf')
        for r in range(n):
            cur += arr[r]
            while cur > target:
                cur -= arr[l]
                l += 1
            if cur == target:
                length = r - l + 1
                if l > 0 and dp[l - 1] != float('inf'):
                    res = min(res, length + dp[l - 1])
                min_l = min(min_l, length)
            dp[r] = min_l
        return res if res != float('inf') else -1