class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        s, e = [], []
        for i, j in intervals:
            s += [i]
            e += [j]
        s.sort()
        e.sort()
        j = 0
        ans = 0
        for i in s:
            if i < e[j]: 
                ans += 1
            else:
                j += 1
        return ans
