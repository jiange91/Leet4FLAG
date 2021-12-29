class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        dq = collections.deque(['', '0', '1', '8'])
        lrs = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        ans = 0
        l = int(low)
        h = int(high)
        while dq:
            lst = dq.popleft()
            if len(lst) > len(high):
                break
            if len(lst) > 1 and lst[0] != '0' and l <= int(lst) <= h:
                ans += 1
            if len(lst) == 1 and l <= int(lst) <= h:
                ans += 1
            for i, j in lrs.items():
                tmp = i + lst + j
                dq.append(tmp)
        return ans
                
