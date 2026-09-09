class Solution:
    def countCommas(self, n: int) -> int:
        comma = 0
        l = [10**3, 10**6, 10**9, 10**12, 10**15]
        
        for i, j in enumerate(l):
            if n >= j:
                end = min(n, l[i + 1] - 1) if i + 1 < len(l) else n
                c = end - j + 1
                comma += c * (i + 1)
            else:
                break
                
        return comma
