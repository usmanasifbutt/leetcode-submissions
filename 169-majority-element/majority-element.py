class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        item = nums[0]
        count = 0
        for i in nums:
            if i == item:
                count += 1
            elif count == 0 and i != item:
                item = i
                count += 1
            else:
                count -= 1

        return item
