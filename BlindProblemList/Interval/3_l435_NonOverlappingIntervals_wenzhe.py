# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         intervals.sort(key = lambda x: x[0])
#         result = [1 for i in range(len(intervals))]

#         def isMerge(interval1, interval2):
#             if interval1[0] >= interval2[1] or interval1[1] <= interval2[0]:
#                 return False
#             return True
        
#         for i in range(1,len(intervals)):
#             cur_i = i-1
#             while cur_i >= 0 and isMerge(intervals[i],intervals[cur_i]):
#                 cur_i -= 1
#             if cur_i >= 0:
#                 result[i] = result[cur_i] + 1

#         return len(intervals) - max(result)

# DP N^2 solution, not passing due to time limit in Python


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        result = []

        def isMerge(interval1, interval2):
            if interval1[0] >= interval2[1] or interval1[1] <= interval2[0]:
                return False
            return True
        
        for i in intervals:
            if len(result) == 0:
                result.append(i)
            else:
                if isMerge(result[-1], i):
                    if result[-1][1] > i[1]:
                        result.pop()
                        result.append(i)
                else:
                    result.append(i)
                
        return len(intervals) - len(result)


# Greedy N*log(N)
