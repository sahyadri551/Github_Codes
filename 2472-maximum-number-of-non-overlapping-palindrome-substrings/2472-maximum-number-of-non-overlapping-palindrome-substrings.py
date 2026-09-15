class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n, ans, m = len(s), 0, -1
        for c in range(2 * n - 1):
            l = c // 2
            r = l + (c % 2)
            while l > m and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    ans += 1
                    m = r
                    break
                l -= 1
                r += 1
        return ans
