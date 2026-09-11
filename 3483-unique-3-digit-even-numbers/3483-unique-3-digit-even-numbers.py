from collections import Counter
class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        available = Counter(digits)
        ans = 0
        for val in range(100, 1000, 2):
            h, t, u = val // 100, (val // 10) % 10, val % 10
            needed = Counter([h, t, u])
            valid = True
            for k, v in needed.items():
                if available[k] < v:
                    valid = False
                    break
            if valid:
                ans += 1
                
        return ans
