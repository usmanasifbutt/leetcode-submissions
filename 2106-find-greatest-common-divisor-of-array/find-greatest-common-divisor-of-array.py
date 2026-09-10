class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_ = float('inf')
        max_ = float('-inf')
        for i in nums:
            min_ = min(min_, i)
            max_ = max(max_, i)

        while min_ != 0: 
            min_, max_ = max_ % min_, min_ 

        return max_