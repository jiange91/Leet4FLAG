class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Manachar:
        news = '#' + '#'.join(s) + '#'
        lps = [0] * len(news)
        ctr = 0
        for i, c in enumerate(news):
            r = ctr+lps[ctr]
            isup = 2 * ctr - i
            lps[i] = 0 if i > r else min(r - i, lps[isup])
            while i-lps[i]-1 >= 0 and i+lps[i]+1 < len(news) and news[i-lps[i]-1] == news[i+lps[i]+1]:
                lps[i] += 1
            if i + lps[i] > r:
                ctr, r = i, i+lps[i]
        
        ml, ctr = 0, 0
        for i, l in enumerate(lps):
            if ml < l:
                ml, ctr = l, i
        start = (ctr-ml)//2
        l = ml
        return s[start:start+l]
            
        
                
