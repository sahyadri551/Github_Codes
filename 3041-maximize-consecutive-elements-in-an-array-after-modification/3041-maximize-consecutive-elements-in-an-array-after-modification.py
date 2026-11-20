class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp={}
        res=0
        for i in nums:
            dp[i+1]=dp.get(i, 0)+1
            dp[i]=dp.get(i-1,0)+1
            res=max(res,dp[i],dp[i+1])
        return res
