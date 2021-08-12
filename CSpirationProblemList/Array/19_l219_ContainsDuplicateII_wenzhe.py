class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = dict()
        for i,n in enumerate(nums):
            prev_i = num_dict.get(n,-1)
            if prev_i != -1 and i - prev_i <= k:
                return True
            num_dict[n] = i
        return False