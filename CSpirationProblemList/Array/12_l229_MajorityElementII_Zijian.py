class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2, c1, c2 = 0, 1, 0, 0
        for n in nums:
            if n == cand1:
                c1 += 1
            elif n == cand2:
                c2 += 1
            elif not c1:
                cand1 = n
                c1 += 1
            elif not c2:
                cand2 = n
                c2 += 1
            else:
                c1, c2 = c1 - 1, c2 - 1
        return [n for n in [cand1, cand2] if nums.count(n) > len(nums) // 3]
