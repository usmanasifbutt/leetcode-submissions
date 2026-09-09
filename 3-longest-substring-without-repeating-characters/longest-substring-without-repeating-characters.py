class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        max_length = 0
        for idx, i in enumerate(s):
            if i not in seen or seen[i] < left:
                seen[i] = idx
                max_length = max(max_length, idx - left + 1)
                continue

            left = seen[i] + 1
            seen[i] = idx
            max_length = max(max_length, idx - left + 1)

        return max_length