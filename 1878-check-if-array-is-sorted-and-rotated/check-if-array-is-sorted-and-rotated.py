class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        ct = 0

        for i in range(0,n):
            if nums[i] > nums[(i+1)%n]:
                ct = ct + 1

        return ct<=1