class Solution:
    def shortestPalindrome(self, s: str) -> str:
        news = '#'.join('?{}!'.format(s))
        l = len(news)
        ctr = 0
        lps = [0] * l
        for i in range(1, l-1):
            r = ctr + lps[ctr]
            if i < r:
                lps[i] = min(lps[2 * ctr - i], r-i)
            while news[i-lps[i]-1] == news[i+lps[i]+1]:
                lps[i] += 1
            if i + lps[i] > r:
                ctr = i
        ml = 0
        for i, l in enumerate(lps):
            if i - l == 1 and ml < l:
                ctr, ml = i, l
        r = (ctr+ml) // 2
        return s[:r-1:-1] + s
            
            
                
