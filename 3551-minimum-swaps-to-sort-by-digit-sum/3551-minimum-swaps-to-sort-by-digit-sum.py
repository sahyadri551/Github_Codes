class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def d(x):
            s=0
            while x:
                s+=x%10
                x//=10
            return s
        n=len(nums)
        a=sorted([(nums[i],i) for i in range(n)], key=lambda x:(d(x[0]),x[0]))
        vis=[False]*n
        ans=0
        for i in range(n):
            if vis[i] or a[i][1]==i:
                continue
            cnt=0
            j=i
            while not vis[j]:
                vis[j]=True
                j=a[j][1]
                cnt+=1
            if cnt > 1:
                ans+=cnt - 1
        return ans
