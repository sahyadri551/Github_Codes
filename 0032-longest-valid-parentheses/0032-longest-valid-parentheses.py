class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ml = 0
        st = [-1]
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ml = max(ml, i - st[-1])
        return ml
