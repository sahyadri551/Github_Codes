class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 2:
            return l
        n=0
        m=0
        for i in range(len(nums)):
            if nums[i] > nums[n]:
                n = i
            if nums[i] < nums[m]:
                m = i
        fmax=max(m,n)+1
        bmax=l-min(m,n)
        both = (min(m, n) + 1) + (l - max(m, n))
        return  min(fmax, bmax, both)
        