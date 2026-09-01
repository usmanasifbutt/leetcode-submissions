class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        length = len(nums)
        for right in range(length):
            if nums[right] == 0:
                continue

            nums[left], nums[right] = nums[right], nums[left]
            left += 1

        return nums

                    
