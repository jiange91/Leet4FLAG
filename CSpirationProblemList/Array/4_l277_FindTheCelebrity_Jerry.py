# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    
    def findCelebrity(self, n: int) -> int:
        self.n = n
        for i in range(n):
            if self.is_celebrity(i):
                return i
        return -1

    def is_celebrity(self, a):
        for b in range(self.n):
            if a == b:
                continue
            if not knows(b, a) or knows(a, b):
                return False
        return True
