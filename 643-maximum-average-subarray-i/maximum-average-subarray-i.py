class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_avg = float('-inf')
        left = 0
        window = 0
        for right in range(len(nums)):
            window += nums[right]
            if right - left + 1 == k:
                avg = window / k
                window -= nums[left]
                left += 1
                max_avg = max(avg, max_avg)

        return max_avg
