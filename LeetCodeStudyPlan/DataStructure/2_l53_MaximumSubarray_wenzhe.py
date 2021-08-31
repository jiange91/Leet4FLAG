class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def merge(l, r):
            if l == r:
                return nums[l], nums[l], nums[l], nums[l]
            mid = (l + r) // 2
            ll, lm, lr, lw = merge(l, mid)
            rl, rm, rr, rw = merge(mid + 1, r)
            
            nl = max(ll, lw + rl)                   # Best starting from left
            nr = max(rr, rw + lr)                   # Best ending with right
            nw = lw + rw                            # All sum together
            nm = max(lm, rm, nl, nr, nw, lr + rl)   # Best in this range
            
            return nl, nm, nr, nw
        
        return merge(0, len(nums)-1)[1]