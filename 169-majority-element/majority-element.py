class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        ele = 0

        for i in range(0,n):
            if cnt == 0:
                cnt = 1
                ele = nums[i]
            elif ele == nums[i]:
                cnt += 1
            else:
                cnt -= 1
    
        cnt1 = nums.count(ele)

        if cnt1 > n//2:
            return ele

        return -1