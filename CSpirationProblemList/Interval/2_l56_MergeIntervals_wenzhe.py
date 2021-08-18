class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        
        def merge(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
        
        def isMerge(interval1, interval2):
            if interval1[0] > interval2[1] or interval1[1] < interval2[0]:
                return False
            return True
        
        idx = 0
        while idx < len(intervals):
            cur_interval = intervals[idx]
            idx += 1
            while idx < len(intervals) and isMerge(cur_interval, intervals[idx]):
                cur_interval = merge(cur_interval, intervals[idx])
                idx += 1
            result.append(cur_interval)            
        
        
        return result