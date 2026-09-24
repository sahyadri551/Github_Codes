class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if sum(int(j) for j in str(n)) == i:
                return i
        return -1
