class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        j=k
        nums=set(nums)
        while j in nums:
            j+=k

        return j
