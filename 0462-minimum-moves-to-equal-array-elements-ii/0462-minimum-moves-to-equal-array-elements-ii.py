class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        m = nums[len(nums) // 2]
        ans = 0
        for i in nums:
            ans += abs(i - m)
        return ans
