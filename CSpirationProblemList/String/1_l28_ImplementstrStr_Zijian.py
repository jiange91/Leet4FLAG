class Solution:
    def strStr(self, hstk: str, ndl: str) -> int:
        if len(ndl) is 0:
            return 0
        # l = len(needle)
        # for i in range(len(haystack)):
        #     if i + l > len(haystack):
        #         return -1
        #     if haystack[i:i+l] == needle:
        #         return i
        # return -1
        lps = self.lps(ndl)
        ans = -1
        # print(lps)
        i, j = 0, 0
        while (i <= len(hstk) and j <= len(ndl)):
            if j == len(ndl):
                return i - len(ndl)
            if i == len(hstk):
                return -1
            if hstk[i] == ndl[j]:
                i = i + 1
                j = j + 1
            elif j == 0:
                i = i + 1
            else:
                j = lps[j-1]
    
    def lps(self, ndl):
        rel = [0] * len(ndl)
        i = 1
        l = 0
        while i < len(ndl):
            if ndl[i] == ndl[l]:
                l = l + 1
                rel[i] = l
                i = i + 1
            elif l == 0:
                rel[i] = 0
                i = i + 1
            else:
                l = rel[l-1]
        return rel
        