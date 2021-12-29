class Solution:
    def reverseVowels(self, s: str) -> str:
        p = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i, j = 0, len(s) - 1
        l = ""
        r = ""
        while i < j:
            # print("{} : {}".format(l, r))
            while i < j and s[i] not in p:
                l = l + s[i]
                i = i + 1
            while j > i and s[j] not in p:
                r = s[j] + r
                j = j - 1
            if i < j:
                l = l + s[j]
                r = s[i] + r
                i = i + 1
                j = j - 1
        if i == j:
            return l + s[j] + r
        else:
            return l + r
