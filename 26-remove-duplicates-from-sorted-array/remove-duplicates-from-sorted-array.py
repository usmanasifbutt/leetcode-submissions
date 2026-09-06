class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        seen = set()
        for idx, i in enumerate(nums):
            if i in seen:
                continue
            
            nums[k] = i
            k += 1
            seen.add(i)
        return k