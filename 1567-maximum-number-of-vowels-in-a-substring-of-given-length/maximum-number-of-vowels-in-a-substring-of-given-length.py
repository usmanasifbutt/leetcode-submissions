class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_ = 0
        left = 0
        window = 0
        vowels = set("aeiou")
        for right in range(len(s)):
            if s[right] in vowels:
                window += 1

            if right - left + 1 > k:
                if s[left] in vowels:
                    window -= 1
                left += 1

            max_ = max(max_, window)
        return max_