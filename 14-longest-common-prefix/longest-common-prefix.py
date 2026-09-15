class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_ = 0
        for i, chars in enumerate(zip(*strs)):
            len_ += 1
            if len(set(chars)) > 1:
                return strs[0][:i]
        
        return strs[0][:len_]
