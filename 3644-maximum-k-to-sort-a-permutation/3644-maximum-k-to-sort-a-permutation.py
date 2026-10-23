class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1
        for i, v in enumerate(nums):
            if i != v:
                k = v if k == -1 else k & v
        return max(0, k)
