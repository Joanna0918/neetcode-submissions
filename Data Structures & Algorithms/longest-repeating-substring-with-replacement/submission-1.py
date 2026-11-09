class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l, r = 0, 0
        mostFreq, res = 0, 0

        while l <= r and r < len(s):
            count[s[r]] += 1
            mostFreq = max(mostFreq, count[s[r]])

            replacements = (r - l + 1) - mostFreq
            while l <= r and replacements > k: 
                count[s[l]] -= 1
                l += 1
                mostFreq = max(mostFreq, count[s[l]])
                replacements = (r - l + 1) - mostFreq
            res = max(res, r - l + 1)
            r += 1
        return res