class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        
        intervals.sort(key=lambda x: x[0])
        
        def isMerge(interval1, interval2):
            if interval1[0] >= interval2[1] or interval1[1] <= interval2[0]:
                return False
            return True
        
        prev = intervals[0]
        
        for i in intervals[1:]:
            if isMerge(i,prev):
                return False
            prev = i
            
        return True