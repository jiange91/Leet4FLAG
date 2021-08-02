class Solution:
    def countBits(self, num: int) -> List[int]:
        ones = [0]
        if num == 0:
            return ones
        
        for n in range(1, num+1):
            ones.append(ones[n>>1])
            if n % 2 != 0:
                ones[-1] += 1
        return ones