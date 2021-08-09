class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur_idx = 0
        for cur_val in nums:
            if cur_val != val:
                nums[cur_idx] = cur_val
                cur_idx += 1
        for i in range(len(nums) - cur_idx):
            nums.pop()