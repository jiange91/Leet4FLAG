class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == None or len(nums) < 3:
            return
        cur_idx = 0
        prev_val = nums[0]-1
        prev_prev_val = nums[0]-2
        for cur_val in nums:
            if cur_val != prev_val or cur_val != prev_prev_val:
                nums[cur_idx] = cur_val
                cur_idx += 1
            prev_val, prev_prev_val = cur_val, prev_val
        for i in range(len(nums) - cur_idx):
            nums.pop()