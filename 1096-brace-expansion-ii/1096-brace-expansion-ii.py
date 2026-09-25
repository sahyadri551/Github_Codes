class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(s: str) -> set[str]:
            if not s:
                return {""}
            
            if s[0] != '{':
                i = 0
                while i < len(s) and s[i].isalpha():
                    i += 1
                left = {s[:i]}
                right = parse(s[i:])
                return {x + y for x in left for y in right}
            
            cnt = 0
            i = 0
            while i < len(s):
                if s[i] == '{': cnt += 1
                elif s[i] == '}': cnt -= 1
                if cnt == 0:
                    break
                i += 1
                
            inside = s[1:i]
            tail = s[i+1:]
            
            parts = []
            start = 0
            lvl = 0
            for j in range(len(inside)):
                if inside[j] == '{': lvl += 1
                elif inside[j] == '}': lvl -= 1
                elif inside[j] == ',' and lvl == 0:
                    parts.append(inside[start:j])
                    start = j + 1
            parts.append(inside[start:])
            
            left = set()
            for p in parts:
                left |= parse(p)
                
            right = parse(tail)
            return {x + y for x in left for y in right}

        return sorted(list(parse(expression)))
