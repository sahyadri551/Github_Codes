class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        counts = Counter(s)
        odd_chars = [ch for ch, count in counts.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        mid = odd_chars[0] if odd_chars else ""
        half_counts = {ch: count // 2 for ch, count in counts.items() if count // 2 > 0}
        n = len(s)
        m = n // 2
        first_half = []
        already_greater = False
        for i in range(m):
            chosen = False
            for idx in range(26):
                c = chr(ord('a') + idx)
                if half_counts.get(c, 0) <= 0:
                    continue
                if already_greater:
                    half_counts[c] -= 1
                    first_half.append(c)
                    chosen = True
                    break
                else:
                    if c < target[i]:
                        continue
                    elif c > target[i]:
                        half_counts[c] -= 1
                        first_half.append(c)
                        already_greater = True
                        chosen = True
                        break
                    else:
                        half_counts[c] -= 1
                        first_half.append(c)
                        rem_chars = []
                        for ch in sorted(half_counts.keys(), reverse=True):
                            rem_chars.extend([ch] * half_counts[ch])
                        temp_first = "".join(first_half) + "".join(rem_chars)
                        max_palindrome = temp_first + mid + temp_first[::-1]
                        if max_palindrome > target:
                            chosen = True
                            break
                        first_half.pop()
                        half_counts[c] += 1
            if not chosen:
                return ""
        ans_first = "".join(first_half)
        ans = ans_first + mid + ans_first[::-1]
        
        return ans if ans > target else ""

        