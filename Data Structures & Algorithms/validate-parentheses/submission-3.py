class Solution:
    def isValid(self, s: str) -> bool:
        stack =  []
        d = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if len(stack) == 0 or d[c] != stack[-1]:
                    return False
                stack.pop()

        return True if len(stack) == 0 else False