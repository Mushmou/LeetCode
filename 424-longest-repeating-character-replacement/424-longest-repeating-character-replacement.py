class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = collections.defaultdict(int)
        res = 0
        for right in range(len(s)):
            window_length = right - left + 1
            freq[s[right]] += 1
            if window_length - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            else:
                res = max(res, window_length)
        return res