class Solution:
    def longestConsecutive(self, nums):
        res = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                cur_len = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    cur_len += 1

                res = max(res, cur_len)

        return res