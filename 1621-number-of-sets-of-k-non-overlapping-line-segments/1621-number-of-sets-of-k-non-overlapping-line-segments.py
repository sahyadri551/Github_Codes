import math
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        total = n + k - 1
        choose = 2 * k
        if choose > total:
            return 0
        return math.comb(total, choose) % MOD