class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        q = [("", 0, 0)]
        for _ in range(2 * n):
            nxt = []
            for s, o, c in q:
                if o < n:
                    nxt.append((s + '(', o + 1, c))
                if c < o:
                    nxt.append((s + ')', o, c + 1))
            q = nxt
        return [s for s, o, c in q]
