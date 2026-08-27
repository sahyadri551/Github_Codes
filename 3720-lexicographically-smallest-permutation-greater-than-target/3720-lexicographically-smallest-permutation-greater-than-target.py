from collections import Counter
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)
        res = []
        limit = 0
        for i in range(n):
            ch = target[i]
            if freq[ch] > 0:
                freq[ch] -= 1
                res.append(ch)
                limit += 1
            else:
                break
        for i in range(limit, -1, -1):
            if i == n:
                freq[res.pop()] += 1
                continue
            curr = target[i]
            ok = False
            for code in range(ord(curr) + 1, ord('z') + 1):
                nxt = chr(code)
                if freq[nxt] > 0:
                    freq[nxt] -= 1
                    res.append(nxt)
                    ok = True
                    break
            if ok:
                for code in range(ord('a'), ord('z') + 1):
                    c = chr(code)
                    if freq[c] > 0:
                        res.extend([c] * freq[c])
                return "".join(res)
            
            if i > 0:
                freq[res.pop()] += 1
        return "" 