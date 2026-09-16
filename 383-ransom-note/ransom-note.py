class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_ = dict()
        for i in magazine:
            map_[i] = map_.get(i, 0) + 1

        for j in ransomNote:
            item = map_.get(j, 0)
            if item == 0:
                return False
            map_[j] = item - 1

        return True