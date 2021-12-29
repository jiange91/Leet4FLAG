# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.tmpbuf = [''] * 4
        self.l = 0
        self.r = 0
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while True:
            if i == n:
                return i
            if self.l >= self.r:
                cur = read4(self.tmpbuf)
                if cur == 0:
                    return i
                self.l = 0
                self.r = cur
            buf[i] = self.tmpbuf[self.l] 
            i += 1
            self.l += 1
            
            
            
