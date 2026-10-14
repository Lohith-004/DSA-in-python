class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[write],nums[fast] = nums[fast], nums[write]
                write += 1
        