class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nums = [i for i in range(n)]
        for x, y in edges:
            tmp = x
            while nums[x] != x: x = nums[x]
            nums[tmp] = x
            tmp = y
            while nums[y] != y: y = nums[y]
            nums[tmp] = y
            if x != y:
                n -= 1
                nums[x] = y
        return n
