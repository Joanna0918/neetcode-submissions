class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0

        for i in range(len(s)):
            # odd
            j = 0
            while (i - j >= 0 and i + j < len(s) 
                and s[i - j] == s[i + j]):
                if (i + j) - (i - j) + 1 > resLen:
                    res = s[i - j : i + j + 1]
                    resLen = (i + j) - (i - j) + 1
                j += 1

            # even
            j = 0
            while (i - j >= 0 and i + 1 + j < len(s)
                and s[i - j] == s[i + 1 + j]):
                if (i + 1 + j) - (i - j) + 1 > resLen:
                    res = s[i - j : i + 1 + j + 1]
                    resLen = (i + 1 + j) - (i - j) + 1
                j += 1
        return res