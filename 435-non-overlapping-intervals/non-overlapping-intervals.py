class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        count = 0
        last_end = intervals[0][1]

        for i in range(1,len(intervals)):

            start = intervals[i][0]
            end = intervals[i][1]

            if start >= last_end:
                last_end = end
            else:
                count += 1
        
        return count