class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])

        result = [intervals[0]]

        for i in range(1,len(intervals)):

            start = intervals[i][0]
            end = intervals[i][1]

            last_end = result[-1][1]

            if start <= last_end:
                result[-1][1] = max(last_end, end)
            else:
                result.append(intervals[i])

        return result
