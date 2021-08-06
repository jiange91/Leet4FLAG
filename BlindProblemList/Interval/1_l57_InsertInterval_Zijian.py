class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for pair in intervals:
            if pair[1] < s: 
                left.append(pair)
            elif pair[0] > e: 
                right.append(pair)
            else:
                s = min(s, pair[0])
                e = max(e, pair[1])
        return left + [[s,e]] + right
