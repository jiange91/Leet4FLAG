class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        slots = set()
        for n in nums:
            if n in slots:
                return True
            else:
                slots.add(n)
        return False
