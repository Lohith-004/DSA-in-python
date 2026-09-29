class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        current = []
        result = []

        def backtrack(index):
            result.append(current.copy())

            for i in range(index, len(nums)):
                current.append(nums[i])

                backtrack(i + 1)

                current.pop()

        backtrack(0)
        
        return result
        