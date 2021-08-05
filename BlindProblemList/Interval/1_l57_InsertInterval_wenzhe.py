class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        def merge(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
        
        def isMerge(interval1, interval2):
            if interval1[0] > interval2[1] or interval1[1] < interval2[0]:
                return False
            return True
        
        starting = -1
        ending = len(intervals)
        firstGreater = len(intervals)
        
        for i in range(len(intervals)):
            if firstGreater == len(intervals) and intervals[i][0] > newInterval[0]:
                firstGreater = i
            if isMerge(intervals[i], newInterval):
                if starting == -1:
                    starting = i
                newInterval = merge(intervals[i], newInterval)
            elif starting != -1:
                ending = i
                break
            
        if starting == -1:
            intervals.insert(firstGreater, newInterval)
            return intervals
        
        if ending == len(intervals):
            return intervals[:starting] + [newInterval]
        else:
            return intervals[:starting] + [newInterval] + intervals[ending:]