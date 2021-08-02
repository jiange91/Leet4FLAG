class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = set()
        self.nums = nums
        for i in range(len(self.nums)-2):
            if self.nums[i] > 0:
                break
            if i == 0 or self.nums[i - 1] != nums[i]:
                self.twoSum(i+1, -self.nums[i])
        return self.result
    
    def twoSum(self, i, target: int) -> List[int]:
        j = len(self.nums)-1

        while i < j:
            cur = self.nums[i] + self.nums[j]
            if cur < target:
                i += 1
            elif cur > target:
                j -= 1
            else:
                self.result.add(tuple(sorted([self.nums[i],self.nums[j],-target])))
                i+=1
                j-=1
                while i < j and self.nums[i] == self.nums[i - 1]:
                    i += 1
                while j > i and self.nums[j] == self.nums[j + 1]:
                    j -= 1