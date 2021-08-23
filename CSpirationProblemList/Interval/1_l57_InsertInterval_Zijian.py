class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        ans = []
        i = 0
        while i < len(intervals):
            si, ei = intervals[i]
            if ei < s:
                ans.append(intervals[i])
            elif e < si:
                break
            else:
                s = min(si, s)
                e = max(ei, e)
            i += 1
        ans.append([s,e])
        if i < len(intervals):
            ans += intervals[i:]
        return ans
