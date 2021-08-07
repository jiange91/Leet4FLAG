class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        order = []
        seen = set()
        res = 0
        for c in s:
            if c in seen:
                idx = 0
                while idx != len(order):
                    if order[idx] != c:
                        seen.remove(order[idx])
                        idx += 1
                    else:
                        idx += 1
                        break
                order = order[idx:]
                order.append(c)
            else:
                order.append(c)
                seen.add(c)
            res = max(res, len(order))
        return res