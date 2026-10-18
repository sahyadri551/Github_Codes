import math

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        M = 10**9 + 7
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            l = [x for x in arr if x < root]
            r = [x for x in arr if x > root]
            return (math.comb(len(l) + len(r), len(l)) * dfs(l) * dfs(r)) % M
        return (dfs(nums) - 1) % M
