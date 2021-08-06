class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        prev = float('-inf')
        for pair in sorted(intervals, key = lambda i : i[0]):
            if pair[0] < prev: return False
            else: prev = pair[1]
        return True
