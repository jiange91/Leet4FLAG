class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        stk = []
        used = set()
        for c in s:
            if c in used:
                counter[c] = counter[c] - 1
                continue
            while stk and counter[stk[-1]] > 0 and stk[-1] > c:
                p = stk.pop()
                used.remove(p)
            stk.append(c)
            used.add(c)
            counter[c] = counter[c] - 1
        ans = ""
        for c in stk:
            ans = ans + c
        return ans
