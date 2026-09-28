class Solution:
    def maxDepth(self, s: str) -> int:
        m=0
        t=0
        for i in s:
            if i=="(":
                t+=1
                m=max(t,m)
            elif i==")":
                
                t-=1
        return m