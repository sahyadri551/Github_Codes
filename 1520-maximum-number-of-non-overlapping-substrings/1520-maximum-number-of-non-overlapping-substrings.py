class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {c: i for i, c in reversed(list(enumerate(s)))}
        last = {c: i for i, c in enumerate(s)}
        
        valid = []
        for c in set(s):
            l, r = first[c], last[c]
            i = l
            possible = True
            while i <= r:
                if first[s[i]] < l:
                    possible = False
                    break
                r = max(r, last[s[i]])
                i += 1
            if possible:
                valid.append((l, r))     
        valid.sort(key=lambda x: x[1])
        ans = []
        last_r = -1
        for l, r in valid:
            if l > last_r:
                ans.append(s[l:r+1])
                last_r = r
        return ans
