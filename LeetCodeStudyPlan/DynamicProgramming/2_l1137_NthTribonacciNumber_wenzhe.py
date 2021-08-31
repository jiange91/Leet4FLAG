class Solution:
    def tribonacci(self, n: int) -> int:
        results = [0,1,1]
        if n <= 2:
            return results[n]
        for _ in range(n - 2):
            results.append(results[-1]+results[-2]+results[-3])
        return results[-1]