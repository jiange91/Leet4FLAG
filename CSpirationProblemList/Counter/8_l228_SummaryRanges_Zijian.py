class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not len(nums): return []
        ans = []
        start, end = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if end > start:
                    ans.append('{}->{}'.format(start, end))
                else:
                    ans.append(str(start))
                start = end = nums[i]
        ans.append('{}->{}'.format(start, end) if end > start else str(start))
        return ans
