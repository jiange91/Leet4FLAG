class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        ds = self.countAndSay(n-1)
        ans = ""
        slow, fast = 0, 0
        while fast < len(ds):
            while fast < len(ds) and ds[fast] == ds[slow]:
                fast = fast + 1
            ans = ans + str(fast-slow) + str(ds[slow])
            slow = fast
        return ans
