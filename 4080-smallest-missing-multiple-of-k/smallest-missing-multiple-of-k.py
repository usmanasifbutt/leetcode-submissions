class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n_set = set(nums)
        index = 1
        while True:
            multiple = k * index
            if multiple in n_set:
                index += 1
                continue
        
            return multiple
            