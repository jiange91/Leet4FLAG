class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = 1
        up, peak, down = 0, 0, 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                up += 1
                peak = up
                ans += 1 + up
                down = 0
            elif ratings[i] == ratings[i-1]:
                ans += 1
                up, peak, down = 0, 0, 0
            else:
                up = 0
                down += 1
                ans += down + (0 if peak >= down else 1)
        return ans
