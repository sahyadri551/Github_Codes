class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            ok = True
            p_max = -1
            for s in range(0, n, k):
                b = nums[s:s+k]
                b_min = min(b)
                b_max = max(b)
                dr = 0
                for i in range(k - 1):
                    if b[i] > b[i+1]:
                        dr += 1
                if b[-1] > b[0]:
                    dr += 1
                if dr > 1 or (p_max != -1 and p_max > b_min):
                    ok = False
                    break
                p_max = b_max
            if ok:
                ans += k
        return ans
