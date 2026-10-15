class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        s=0
        for i in range(n):
            t=set()
            for j in range(i,n):
                t.add(nums[j])
                l=len(t)
                s=s+(l**2)
        return s