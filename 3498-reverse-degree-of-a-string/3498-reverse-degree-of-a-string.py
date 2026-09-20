class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s, 1):
            j = 26 - (ord(c) - 97)
            ans += j * i
        return ans
