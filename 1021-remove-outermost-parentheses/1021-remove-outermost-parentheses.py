class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        r = []
        c = 0
        for ch in s:
            if ch == '(':
                if c > 0:
                    r.append(ch)
                c += 1
            else:
                c -= 1
                if c > 0:
                    r.append(ch)
        return "".join(r)