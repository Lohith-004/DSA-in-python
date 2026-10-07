class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        left_rem = 0
        right_rem = 0

        for ch in s:
            if ch == '(':
                left_rem += 1

            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        result = set()

        def backtrack(index, left_count, right_count,
                      left_rem, right_rem, path):

            # End of string
            if index == len(s):

                if left_rem == 0 and right_rem == 0:
                    result.add("".join(path))

                return

            ch = s[index]

            # Option 1: Remove current parenthesis
            if ch == '(' and left_rem > 0:
                backtrack(
                    index + 1,
                    left_count,
                    right_count,
                    left_rem - 1,
                    right_rem,
                    path
                )

            elif ch == ')' and right_rem > 0:
                backtrack(
                    index + 1,
                    left_count,
                    right_count,
                    left_rem,
                    right_rem - 1,
                    path
                )

            # Option 2: Keep current character
            path.append(ch)

            if ch != '(' and ch != ')':
                backtrack(
                    index + 1,
                    left_count,
                    right_count,
                    left_rem,
                    right_rem,
                    path
                )

            elif ch == '(':
                backtrack(
                    index + 1,
                    left_count + 1,
                    right_count,
                    left_rem,
                    right_rem,
                    path
                )

            elif ch == ')' and right_count < left_count:
                backtrack(
                    index + 1,
                    left_count,
                    right_count + 1,
                    left_rem,
                    right_rem,
                    path
                )

            path.pop()

        backtrack(
            0,
            0,
            0,
            left_rem,
            right_rem,
            []
        )

        return list(result)