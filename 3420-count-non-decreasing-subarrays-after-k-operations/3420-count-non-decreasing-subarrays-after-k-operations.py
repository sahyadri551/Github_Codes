class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        c = 0
        q = []
        h = 0
        j = n - 1
        for i in range(n - 1, -1, -1):
            cnt = 1
            while len(q) > h and q[-1][0] < nums[i]:
                val, length = q.pop()
                c += (nums[i] - val) * length
                cnt += length
            q.append([nums[i], cnt])
            while c > k:
                c -= q[h][0] - nums[j]
                q[h][1] -= 1
                if q[h][1] == 0:
                    h += 1
                j -= 1
            ans += j - i + 1
        return ans
