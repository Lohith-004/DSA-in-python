class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                
                val = stack.pop()

                if val == '(' and ch == ')' or val == '[' and ch == ']' or val == '{' and ch == '}':
                    continue
                else:
                    return False
        
        return len(stack) == 0
        