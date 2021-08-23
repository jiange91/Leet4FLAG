class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for pair in sorted(intervals, key=lambda i: i[0]):
            if ans and ans[-1][1] >= pair[0]:
                ans[-1][1] = max(ans[-1][1], pair[1])
            else:
                ans.append(pair)
        return ans
                
