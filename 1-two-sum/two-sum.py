class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(1,n):
            for j in range(i,n):
                if nums[j] + nums[j-i] == target:
                    return [j-i,j]
                    
        return []
        