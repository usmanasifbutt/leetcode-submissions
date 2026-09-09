class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        commas = 0
        commas_in_range = 1
        start = 1000

        while start <= n:
            next_start = start * 1000
            
            commas += commas_in_range * (min(n, next_start - 1) - start + 1)

            start = next_start
            commas_in_range += 1
        return commas