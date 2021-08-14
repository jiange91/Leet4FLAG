# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        c = 0
        for i in range(n):
            if knows(c, i): 
                c = i
        for i in range(c):
            if knows(c,i):
                return -1
        for i in range(n):
            if not knows(i, c):
                return -1
        return c
