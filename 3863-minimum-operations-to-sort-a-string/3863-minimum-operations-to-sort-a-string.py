class Solution:
    def minOperations(self, s: str) -> int:
        if s == "".join(sorted(s)):
            return 0
        n = len(s)
        if n == 2:
            return -1
        a, b = min(s), max(s)
        if s[0] == a or s[-1] == b:
            return 1
        for i in range(1, n - 1):
            if s[i] == a or s[i] == b:
                return 2
        return 3
