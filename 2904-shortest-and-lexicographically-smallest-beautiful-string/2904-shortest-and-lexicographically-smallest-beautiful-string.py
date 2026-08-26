class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ""
            
        res = ""
        l = 0
        one = 0
        
        for i in range(len(s)):
            if s[i] == '1':
                one += 1
            while one == k and s[l] == '0':
                l += 1
            if one == k:
                substr = s[l:i+1]
                
                if res == "":
                    res = substr
                elif len(substr) < len(res):
                    res = substr
                elif len(substr) == len(res) and substr < res:
                    res = substr
                if s[l] == '1':
                    one -= 1
                l += 1
        return res