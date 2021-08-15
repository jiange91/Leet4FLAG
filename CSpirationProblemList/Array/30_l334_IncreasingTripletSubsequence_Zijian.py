class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ijk = [float('inf')] * 3
        for n in nums:
            if n < ijk[0]:
                ijk[0] = n
            elif ijk[0] < n < ijk[1]:
                ijk[1] = n
            elif ijk[1] < n < ijk[2]:
                return True
        return False
