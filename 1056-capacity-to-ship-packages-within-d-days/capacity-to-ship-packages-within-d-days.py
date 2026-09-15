class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2
            needed = self.daysNeeded(weights,mid)

            if needed <= days:
                high = mid - 1
            else:
                low = mid + 1

        return low

    def daysNeeded(self, weights, capacity):
        days = 1
        currentLoad = 0

        for w in weights:
            if currentLoad + w > capacity:
                days += 1
                currentLoad = w
            else:
                currentLoad += w

        return days
        