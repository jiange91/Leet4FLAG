class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        @cache
        def helper(n):
            if n == 0:
                return [""]
            if n == 1:
                return ['0', '1', '8']
            else:
                tmp = helper(n-2)
                if n >= 4:
                    zerow = helper(n-4)
                    for z in zerow:
                        tmp.append('0' + z + '0')
                ans = []
                for t in tmp:
                    ans.extend(['1' + t + '1', \
                                '6' + t + '9', \
                                '8' + t + '8', \
                                '9' + t + '6'])
                return ans
        if n == 2:
            return ["11","69","88","96"]
        return helper(n)
