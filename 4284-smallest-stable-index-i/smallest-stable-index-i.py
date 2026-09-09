class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefix_max = []
        current_max = float('-inf')
        for x in nums:
            current_max = max(current_max, x)
            prefix_max.append(current_max)

        suffix_min = [0] * len(nums)
        current_min = float('inf')
        for i in range(len(nums) - 1, -1, -1):
            current_min = min(current_min, nums[i])
            suffix_min[i] = current_min

        for idx, i in enumerate(nums):
            l_max = prefix_max[idx]
            r_min = suffix_min[idx]

            if l_max - r_min <= k:
                return idx
            
        return -1