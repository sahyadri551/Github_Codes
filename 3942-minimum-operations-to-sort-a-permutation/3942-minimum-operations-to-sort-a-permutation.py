class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        z = nums.index(0)
        ans = float('inf')
        inc = True
        for j in range(n):
            if nums[(z + j) % n] != j:
                inc = False
                break
        if inc:
            ans = min(ans, z, n - z + 2)
        dec = True
        for j in range(n):
            if nums[(z - j) % n] != j:
                dec = False
                break
        if dec:
            ans = min(ans, z + 2, n - z)
        return ans if ans != float('inf') else -1
