class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        nxt=[{}]
        lnk=[-1]
        ln=[0]
        cnt=[0]
        lst=0
        for x in nums:
            cur=len(nxt)
            nxt.append({})
            lnk.append(0)
            ln.append(ln[lst]+1)
            cnt.append(1)
            p=lst
            while p!=-1 and x not in nxt[p]:
                nxt[p][x]=cur
                p=lnk[p]
            if p==-1:
                lnk[cur]=0
            else:
                q=nxt[p][x]
                if ln[p]+1==ln[q]:
                    lnk[cur]=q
                else:
                    cl=len(nxt)
                    nxt.append(nxt[q].copy())
                    lnk.append(lnk[q])
                    ln.append(ln[p]+1)
                    cnt.append(0)
                    while p!=-1 and nxt[p].get(x)==q:
                        nxt[p][x]=cl
                        p=lnk[p]
                    lnk[q]=lnk[cur]=cl
            lst=cur
        ord=sorted(range(1,len(nxt)),key=lambda i:ln[i],reverse=True)
        for i in ord:
            cnt[lnk[i]]+=cnt[i]
        ans=n
        for i in range(1,len(nxt)):
            if cnt[i]==1:
                ans=min(ans,ln[lnk[i]]+1)
        return ans
