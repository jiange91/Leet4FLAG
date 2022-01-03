class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ds = []
        while x > 0:
            ds.append(x % 10)
            x = x // 10
        i, j = 0, len(ds) - 1
        while i < j:
            if ds[i] != ds[j]:
                return False
            i += 1
            j -= 1
        return True
