class Solution:
    def isPalindrome(self, s: str) -> bool:
        lows = s.lower()
        aln = "".join([c for c in lows if c.isalnum()])
        i, j = 0, len(aln) - 1
        while i < j:
            if aln[i] != aln[j]:
                return False
            i += 1
            j -= 1
        return True
