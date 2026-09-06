class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        seen = {}
        for idx, i in enumerate(nums):
            if seen.get(i) and seen.get(i) >= 2:
                continue
            
            nums[k] = i
            k += 1
            seen[i] = seen.get(i, 0) + 1
        
        return k