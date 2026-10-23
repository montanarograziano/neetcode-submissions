class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c != ']':
                stack.append(c)
            else:
                cur = ""
                while stack and stack[-1] != '[':
                    cur = stack.pop() + cur
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * cur)
        
        return "".join(stack)
                
        