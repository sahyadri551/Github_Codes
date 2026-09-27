class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for i in s:
            if i == ')':
                seg = []
                while st and st[-1] != '(':
                    seg.append(st.pop())
                st.pop()
                st.extend(seg)
            else:
                st.append(i)
        return "".join(st)
