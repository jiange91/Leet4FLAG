class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []

        def add(low, high):
            if low > high:
                return
            if low == high:
                result.append(str(low))
            else:
                result.append(str(low) + '->' + str(high))

        if not nums: # edge case
            add(lower, upper)
            return result

        add(lower, nums[0] - 1)

        for x in range(len(nums)):
            add(nums[x - 1] + 1, nums[x] - 1)

        add(nums[-1] + 1, upper)

        return result