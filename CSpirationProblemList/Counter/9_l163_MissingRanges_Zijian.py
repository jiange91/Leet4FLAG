class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        cur = lower
        for n in nums:
            if n == cur:
                cur += 1
            elif n < cur:
                continue
            else:
                ans.append(str(cur) if n-1 == cur else "{}->{}".format(cur, n-1))
                cur = n + 1
        if cur <= upper:
            ans.append(str(cur) if upper == cur else "{}->{}".format(cur, upper))
        return ans
                
