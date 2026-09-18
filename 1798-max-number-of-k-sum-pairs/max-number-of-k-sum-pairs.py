class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = dict()
        ops = 0
        for i in nums:
            diff = k - i
            if diff in seen and seen[diff] > 0:
                ops += 1
                seen[diff] = seen[diff] - 1
            else:
                seen[i] = seen.get(i, 0) + 1
        return ops