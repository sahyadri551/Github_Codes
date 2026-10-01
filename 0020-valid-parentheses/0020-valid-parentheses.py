class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i in "({[": l.append(i)
            elif (len(l)>0) and ((i==")" and l[-1]=="(") or (i=="}" and l[-1]=="{") or (i=="]" and l[-1]=="[")):
                 l.pop()
            else: return False
        if len(l)==0: return True 
        else: return False