class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt1 = 0
        cnt2 = 0
        ele1 = 0
        ele2 = 0

        for num in nums:
            if num == ele1:
                cnt1 += 1
            elif num == ele2:
                cnt2 += 1
            elif cnt1 == 0:
                ele1 = num
                cnt1 += 1
            elif cnt2 == 0:
                ele2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = 0
        cnt2 = 0

        for num in nums:
            if num == ele1:
                cnt1 += 1
            elif num == ele2:
                cnt2 += 1
        
        result = []

        if cnt1 > n//3:
            result.append(ele1)
        
        if cnt2 > n//3:
            result.append(ele2)
    
        return result
        