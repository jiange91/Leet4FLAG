class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            i1 = a + b
            i2 = b + a
            for c1, c2 in zip(i1, i2):
                if c1 > c2:
                    return 1
                if c1 < c2:
                    return -1
            return 0
            
        snums = [str(n) for n in nums]
        ssnums = sorted(snums, key=functools.cmp_to_key(cmp), reverse=True)
        ans = ""
        if ssnums[0] == '0':
            return '0'
        for i in ssnums:
            ans = ans + i
        return ans
