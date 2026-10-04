class Solution:
    def checkValidString(self, s: str) -> bool:
        i = j = 0
        for c in s:
            i += 1 if c == '(' else -1
            j += 1 if c != ')' else -1
            if j < 0: 
                return False
            i = max(i, 0)
        return i == 0
