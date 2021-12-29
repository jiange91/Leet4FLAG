class Solution:
    def canConstruct(self, rsn: str, mgz: str) -> bool:
        slots = {}
        for c in mgz:
            if c not in slots:
                slots[c] = 1
            else:
                slots[c] = slots[c] + 1
        for c in rsn:
            if c not in slots or slots[c] == 0:
                return False
            slots[c] = slots[c] - 1
        return True
