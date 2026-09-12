class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        arr = []
        for i, (s, e, w) in enumerate(intervals):
            arr.append((s, e, w, i))
        
        arr.sort()
        n = len(arr)
        
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        
        def get_next(end_time):
            low, high = 0, n
            while low < high:
                mid = (low + high) // 2
                if arr[mid][0] > end_time:
                    high = mid
                else:
                    low = mid + 1
            return low

        for i in range(n - 1, -1, -1):
            s, e, w, orig_i = arr[i]
            nxt = get_next(e)
            
            for k in range(1, 5):
                skip_w, skip_ids = dp[i + 1][k]
                
                take_w, take_ids = dp[nxt][k - 1]
                cur_w = w + take_w
                cur_ids = tuple(sorted((orig_i,) + take_ids))
                
                if cur_w > skip_w:
                    dp[i][k] = (cur_w, cur_ids)
                elif cur_w < skip_w:
                    dp[i][k] = (skip_w, skip_ids)
                else:
                    if cur_ids < skip_ids:
                        dp[i][k] = (cur_w, cur_ids)
                    else:
                        dp[i][k] = (skip_w, skip_ids)
                        
        return list(dp[0][4][1])
