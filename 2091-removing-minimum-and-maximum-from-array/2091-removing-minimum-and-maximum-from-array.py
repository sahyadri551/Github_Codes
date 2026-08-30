class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)
        del_left = right + 1
        del_right = n - left
        del_both = (left + 1) + (n - right)
        return min(del_left, del_right, del_both)
