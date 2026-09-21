class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_ = 0
        for idx, i in enumerate(s):
            if i == "(":
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    max_ = max(idx - stack[-1], max_)

        return max_