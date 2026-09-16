class Solution:
    def maxArea(self, height: list[int]) -> int:
        area_ = 0
        len_ = len(height)
        
        left = 0
        right = len_ - 1

        for i in range(len_):
            x = right - left
            y = min(height[left], height[right])
            area_ = max(x*y, area_)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area_