class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        t = sum(nums) - x
        if t < 0:
            return -1
        if t == 0:
            return len(nums)
        n = len(nums)
        mx = -1
        curr = 0
        i = 0
        for j in range(n):
            curr += nums[j]
            while curr > t:
                curr -= nums[i]
                i += 1
            if curr == t:
                mx = max(mx, j - i + 1)
        return n - mx if mx != -1 else -1
