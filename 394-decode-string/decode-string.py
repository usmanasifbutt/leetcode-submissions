class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        current_num = 0
        current_str = ""
        
        for i in s:
            if i == "[":
                stack.append((current_num, current_str))
                current_num = 0
                current_str = ""
                continue

            if i == "]" and stack:
                prev_num, prev_str = stack.pop()
                current_str = prev_str + (prev_num * current_str)
                continue

            if i.isdigit():
                if current_num:
                    current_num = current_num * 10 + int(i)
                else:
                    current_num = int(i)
            else:
                current_str += i

        return current_str