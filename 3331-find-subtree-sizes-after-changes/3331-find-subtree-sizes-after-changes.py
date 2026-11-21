class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n=len(parent)
        g=[[] for i in range(n)]
        for i in range(1,n):
            g[parent[i]].append(i)
        last=[-1]*26
        np=list(parent)
        def dfs1(u):
            c=ord(s[u])-97
            prev=last[c]
            if prev!=-1:
                np[u]=prev
            last[c]=u
            for v in g[u]:
                dfs1(v)
            last[c]=prev
        dfs1(0)
        ng=[[] for i in range(n)]
        for i in range(1,n):
            ng[np[i]].append(i)
        ans=[1]*n
        def dfs2(u):
            for v in ng[u]:
                dfs2(v)
                ans[u]+=ans[v]
        dfs2(0)
        return ans
