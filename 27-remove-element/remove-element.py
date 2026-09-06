class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for idx, i in enumerate(nums):
            if i != val:
                nums[k] = i
                k += 1
                continue

        return k

            