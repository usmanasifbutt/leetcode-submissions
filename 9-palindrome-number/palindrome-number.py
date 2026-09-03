class Solution:
    def isPalindrome(self, x: int) -> bool:
        length = 0
        digits = []
        
        if x < 0:
            return False
        
        if x == 0:
            return True

        num = abs(x)
        while num > 0:
            num, remainder = divmod(num, 10)
            digits.append(remainder)
            length += 1
        
        for idx, i in enumerate(digits):
            if idx > length -1:
                break

            if digits[idx] == digits[length - 1]:
                length -= 1
                continue
            
            return False

        return True