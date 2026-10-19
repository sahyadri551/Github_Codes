class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        l = sum(x < target for x in nums)
        r = l + nums.count(target) - 1
        if (l > r) or (target not in nums):
            return [] 
        return [i for i in range(l, r + 1)]
