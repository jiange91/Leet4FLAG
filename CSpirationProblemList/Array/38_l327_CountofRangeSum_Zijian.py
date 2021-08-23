class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pfix = [0]
        for n in nums:
            pfix.append(pfix[-1] + n)
                    
        # [lo, hi)
        def sort(lo, hi):
            mid = lo + (hi - lo) // 2
            if mid == lo:
                return (0, pfix[lo:hi])
            lans, pfixl = sort(lo, mid) 
            rans, pfixr = sort(mid, hi)
            ans = lans + rans
            i = j = mid
            for l in pfix[lo: mid]:
                while i < hi and pfix[i] - l < lower: i += 1
                while j < hi and pfix[j] - l <= upper: j += 1
                ans += j - i
            l, r = 0, 0
            while l < len(pfixl) and r < len(pfixr):
                if pfixl[l] < pfixr[r]:
                    pfix[lo+l+r] = pfixl[l]
                    l += 1
                else:
                    pfix[lo+l+r] = pfixr[r]
                    r += 1
            while l < len(pfixl):
                pfix[lo+l+r] = pfixl[l]
                l += 1
            while r < len(pfixr):
                pfix[lo+l+r] = pfixr[r]
                r += 1
            return (ans, pfix[lo:hi])
        ans, l = sort(0, len(pfix))
        return ans
