class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n=len(items)
        g=[1]*n
        for i in range(n):
            f=items[i][0]
            for j in range(n):
                if i!=j and items[j][0]%f==0:
                    g[i]+=1
        dp=[0]*(budget+1)
        for i in range(n):
            p=items[i][1]
            v=g[i]
            for j in range(budget,p-1,-1):
                if dp[j-p]+v>dp[j]:
                    dp[j]=dp[j-p]+v
        m=min(x[1] for x in items)
        res=0
        for i in range(budget+1):
            c=dp[i]+(budget-i)//m
            if c>res:
                res=c
        return res
