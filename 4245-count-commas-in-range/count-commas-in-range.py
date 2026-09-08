class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        
        commas = 1
        start = 1000
        commas_per_number = 1

        while start <= n:
            next_start = start * 1000
            commas += commas_per_number * min(n, next_start) - start

            start = next_start
            commas_per_number += 1

        return commas