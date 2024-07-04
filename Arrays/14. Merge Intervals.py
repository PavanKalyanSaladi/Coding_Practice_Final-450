'''
56. Merge Intervals
Medium
Topics
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''


def merge(intervals):
        interval = intervals[0]
        non_overlap = []
        if len(intervals) <= 1:
            return intervals
        for current in range(1, len(intervals)):
            if interval[1] >= intervals[current][0] and interval[1] <= intervals[current][1]:
                non_overlap.append([interval[0], intervals[current][1]])
                interval = [interval[0], intervals[current][1]]
            elif interval[1] >= intervals[current][1]:
                non_overlap.append(interval)
            elif interval not in non_overlap:
                 non_overlap.append(interval, current)
                 interval = current
            else:
                non_overlap.append(intervals[current])
                interval = intervals[current]
        return non_overlap

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))



# Solution2 But failing above case
def merge2(intervals):
        interval = intervals[0]
        non_overlap = []
        if len(intervals) <= 1:
            return intervals
        for current in range(1, len(intervals)):
            if interval[1] < intervals[current][0] and interval[1] < intervals[current][1]:
                if interval not in non_overlap:
                    non_overlap.append(interval)
                non_overlap.append(intervals[current])
                interval = intervals[current]
            else:
                non_overlap.append([min(interval[0], intervals[current][0]), max(interval[1], intervals[current][1])])
        return non_overlap

intervals = [[1, 4], [5, 6]]
print(merge2(intervals))
intervals = [[1, 4], [0, 4]]
print(merge2(intervals))