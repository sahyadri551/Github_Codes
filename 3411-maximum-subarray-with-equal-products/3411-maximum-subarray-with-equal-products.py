import math
class Solution:
    def maxLength(self,nums:list[int])->int:
        n=len(nums)
        ans=0
        for i in range(n):
            p=1
            g=0
            l=1
            for j in range(i,n):
                p*=nums[j]
                g=math.gcd(g,nums[j])
                l=math.lcm(l,nums[j])
                if p==l*g:
                    ans=max(ans,j-i+1)
        return ans
