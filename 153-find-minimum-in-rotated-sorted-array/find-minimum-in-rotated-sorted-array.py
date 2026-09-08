class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n -1
        ans = float('inf')

        while low <= high:
            mid = low +(high - low)//2

            if nums[low] <= nums[mid]:
                ans = min(ans,nums[low])
                low = mid + 1
            else:
                high = mid - 1
                ans = min(ans,nums[mid])
        
        return ans