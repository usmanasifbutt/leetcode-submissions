class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_ = 0
        window_ = float('inf')
        for right, val in enumerate(nums):
            sum_ += val
            while sum_ >= target:
                sum_ -= nums[left]
                window_ = min(window_, right - left + 1)
                left += 1
        
        return 0 if window_ == float('inf') else window_