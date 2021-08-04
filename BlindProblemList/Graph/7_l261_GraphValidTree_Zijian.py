class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nums = [-1] * n
        for x, y in edges:
            while nums[x] != -1: x = nums[x]
            while nums[y] != -1: y = nums[y]
            if x == y: return False
            nums[x] = y
        return len(edges) == n - 1
