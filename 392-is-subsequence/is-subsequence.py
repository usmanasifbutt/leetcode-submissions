class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        s_len = len(s)

        for j in t:
            if i < s_len and j == s[i]:
                i += 1

        return s_len == i
