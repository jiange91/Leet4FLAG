# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l ,r = 1, n
        
        while l != r:
            candidate = (l + r) // 2
            res = guess(candidate)
            if res == 0:
                return candidate
            elif res < 0:
                r = candidate
            else: # res > 0
                l = candidate + 1
                
        return l