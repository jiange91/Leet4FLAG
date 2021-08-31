class Solution:
    def fib(self, n: int) -> int:
        results = [0,1]
        if n <= 1:
            return results[n]
        for i in range(n - 1):
            results.append(results[-1]+results[-2])
        return results[-1]