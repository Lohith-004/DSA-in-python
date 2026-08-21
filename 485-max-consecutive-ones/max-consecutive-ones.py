class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max = 0

        for num in nums:
            if num == 1:
                count = count + 1
                if count > max:
                    max = count
            else:
                count = 0

        return max
        