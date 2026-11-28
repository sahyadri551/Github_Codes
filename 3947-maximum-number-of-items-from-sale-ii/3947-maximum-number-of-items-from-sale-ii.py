class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n=len(items)
        cnt=[0]*(n+1)
        for f,p in items:
            cnt[f]+=1
        g=[0]*(n+1)
        for i in range(1,n+1):
            if cnt[i]:
                for j in range(i,n+1,i):
                    g[i]+=cnt[j]
                g[i]-=1
        items.sort(key=lambda x:x[1])
        m=items[0][1]
        ans=0
        for f,p in items:
            if p>=2*m or budget<p:
                break
            k=min(g[f],budget//p)
            ans+=2*k
            budget-=k*p
        ans+=budget//m
        return ans
