class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = sorted([x * x for x in nums])
        n = len(a)
        i, j = 0, n - 1
        ans = 0
        sign = 1
        while i <= j:
            if sign == 1:
                ans += a[j]
                j -= 1
            else:
                ans -= a[i]
                i += 1
            sign *= -1
        return ans
