class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == None or nums == []:
            return
        cur_idx = 0
        prev_val = nums[0]-1
        for cur_val in nums:
            if cur_val != prev_val:
                nums[cur_idx] = cur_val
                cur_idx += 1
            prev_val = cur_val
        for i in range(len(nums) - cur_idx):
            nums.pop()