class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def f(s):
            m, d = map(int, s.split('-'))
            return sum(days[:m-1]) + d
        a1 = f(arriveAlice)
        a2 = f(leaveAlice)
        b1 = f(arriveBob)
        b2 = f(leaveBob)
        start = max(a1, b1)
        end = min(a2, b2)
        return max(0, end - start + 1)
