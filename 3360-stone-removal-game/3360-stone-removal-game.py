class Solution:
    def canAliceWin(self, n: int) -> bool:
        j=0
        for i in range(10,0,-1):
            if n<i:
                break
            n-=i
            j+=1
        return j%2==1