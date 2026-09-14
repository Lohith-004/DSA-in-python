class Solution:
    def sumByD(self, nums, div):
        return sum(math.ceil(x/div) for x in nums)

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if len(nums) > threshold:
            return -1

        low = 1
        high = max(nums)
        ans = -1

        while low <= high:
            mid = (low+high) // 2

            if self.sumByD(nums, mid) <= threshold:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
        