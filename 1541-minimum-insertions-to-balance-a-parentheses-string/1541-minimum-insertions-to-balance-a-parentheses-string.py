class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        req = 0
        for c in s:
            if c == '(':
                req += 2
                if req % 2 == 1:
                    ans += 1
                    req -= 1
            else:
                req -= 1
                if req < 0:
                    ans += 1
                    req += 2
        return ans + req
