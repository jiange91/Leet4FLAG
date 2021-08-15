class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        d = {}
        for i, v in enumerate(nums):
            b = v // (t+1)
            if b in d:
                return True
            elif b-1 in d and abs(nums[d[b-1]] - v) <= t:
                return True
            elif b+1 in d and abs(nums[d[b+1]] - v) <= t:
                return True
            d[b] = i
            if i >= k: del(d[nums[i-k] // (t+1)])
        return False
