class Solution:
    def intToRoman(self, num: int) -> str:
        m = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        d = 10
        ans = ""
        while num > 0:
            r = num % d
            # print(r)
            if r * 10 == 4 * d:
                ans = m[d//10] + m[d//2] + ans
            elif r * 10 == 9 * d:
                ans = m[d//10] + m[d] + ans
            elif r * 10 < 4 * d:
                for i in range(d//10, r+1, d//10):
                    ans = m[d//10] + ans
            elif r * 10 < 9 * d:
                for i in range(d//10, r-d//2+1, d//10):
                    ans = m[d//10] + ans
                ans = m[d//2] + ans
            num = num - r
            d = d * 10
        return ans
            
            
