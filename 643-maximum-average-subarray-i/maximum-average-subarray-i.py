class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_sum = float('-inf')
        left = 0
        window = 0
        for right in range(len(nums)):
            window += nums[right]
            if right - left + 1 == k:
                max_sum = max(window, max_sum)
                window -= nums[left]
                left += 1
        return max_sum / k
