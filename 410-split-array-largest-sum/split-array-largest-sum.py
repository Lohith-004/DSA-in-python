class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low+high) // 2

            partitions = self.count_partitions(nums,mid)

            if partitions > k:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
    
    def count_partitions(self,nums,max_sum):
        partitions = 1
        subarray_sum = 0

        for num in nums:
            if subarray_sum + num <= max_sum:
                subarray_sum += num
            else:
                partitions += 1
                subarray_sum = num
        
        return partitions