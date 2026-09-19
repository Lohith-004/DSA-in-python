class Solution:
    def beautySum(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            freq = {}
            for j in range(i,len(s)):

                freq[s[j]] = freq.get(s[j],0) + 1
                values = freq.values()

                mini = min(values)
                maxi = max(values)

                total += maxi - mini
        
        return total