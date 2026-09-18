class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_ = 0
        left = 0
        window = 0
        window_zeros = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                window += 1
            else:
                window += 1
                window_zeros += 1

            while window_zeros > k:
                if nums[left] == 0:
                    window_zeros -= 1
                window -= 1
                left += 1

            max_ = max(max_, window)
        return max_