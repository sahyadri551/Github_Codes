class Solution:
    def checkString(self, s: str) -> bool:
        f=False
        for i in range(len(s)):
            if s[i]=='b':
                f=True
            elif f and s[i]=='a':
                return False
        return True
