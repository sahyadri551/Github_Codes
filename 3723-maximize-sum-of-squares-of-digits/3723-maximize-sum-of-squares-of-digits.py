class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        k = sum // 9
        r = sum % 9
        res = "9" * k
        if r > 0:
            res += str(r)
        return res + "0" * (num - len(res))
