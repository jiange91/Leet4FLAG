class Solution:
    def __init__(self):
        self.bytes = [-1] * 256
    def reverseBits(self, n: int) -> int:
        mask = 255
        res = 0
        res += self.reverseByte(n & mask)
        for i in range(3):
            res = res << 8
            n = n >> 8
            res += self.reverseByte(n & mask)
        return res
            
        
    def reverseByte(self, n):
        if self.bytes[n] == -1:
            cur_n = n
            res = 0
            res += cur_n & 1
            for i in range(7):
                cur_n = cur_n >> 1
                res = res << 1
                res += cur_n & 1
            self.bytes[n] = res
        return self.bytes[n]