class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i, x in enumerate(nums):
            if n % (i + 1) == 0:
                ans += x * x
        return ans
