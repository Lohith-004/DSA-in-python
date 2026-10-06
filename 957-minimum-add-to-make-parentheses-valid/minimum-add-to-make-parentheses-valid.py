class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        stack = []

        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if len(stack) != 0:
                    stack.pop()
                else:
                    count += 1

        return len(stack) + count