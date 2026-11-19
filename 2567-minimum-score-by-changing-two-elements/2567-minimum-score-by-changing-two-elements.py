class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = float('inf')
        for i in range(3):
            j = n - 3 + i
            ans = min(ans, nums[j] - nums[i])
        return ans
