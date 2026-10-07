class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        rem_l = rem_r = 0
        for char in s:
            if char == '(':
                rem_l += 1
            elif char == ')':
                if rem_l > 0:
                    rem_l -= 1
                else:
                    rem_r += 1
        res = []
        def dfs(idx, l, r, rem_l, rem_r, path):
            if idx == len(s):
                if rem_l == 0 and rem_r == 0:
                    res.append(path)
                return
            if s[idx] == '(':
                if rem_l > 0 and (idx == 0 or s[idx - 1] != '('):
                    for i in range(1, rem_l + 1):
                        if idx + i <= len(s) and all(s[idx + j] == '(' for j in range(i)):
                            dfs(idx + i, l, r, rem_l - i, rem_r, path)
                dfs(idx + 1, l + 1, r, rem_l, rem_r, path + '(')
            elif s[idx] == ')':
                if rem_r > 0 and (idx == 0 or s[idx - 1] != ')'):
                    for i in range(1, rem_r + 1):
                        if idx + i <= len(s) and all(s[idx + j] == ')' for j in range(i)):
                            dfs(idx + i, l, r, rem_l, rem_r - i, path)
                if l > r:
                    dfs(idx + 1, l, r + 1, rem_l, rem_r, path + ')')
            else:
                dfs(idx + 1, l, r, rem_l, rem_r, path + s[idx])
        dfs(0, 0, 0, rem_l, rem_r, "")
        return res
