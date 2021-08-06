class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        c = 0
        itvls = sorted(intervals, key = lambda i : i[0])
        for i in range(1, len(itvls)):
            if itvls[i][0] < itvls[c][1]:
                ans += 1
                c = c if itvls[c][1] < itvls[i][1] else i
            else:
                c = i
        return ans
