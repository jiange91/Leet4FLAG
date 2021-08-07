class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        l = 0
        t_dict = {}
        t_count = len(t)
        for c in t:
            t_dict[c] = t_dict.get(c,0) + 1
        
        res_len = len(s)
        res_str = ''
        
        
        for r, char in enumerate(s):
            if char in t_dict:
                t_dict[char] -= 1
                if t_dict[char] >= 0:
                    t_count -= 1
                if t_count <= 0:
                    for i in range(l,r+1):
                        if s[i] in t_dict:
                            if t_dict[s[i]] >= 0:
                                l = i
                                break
                            else:
                                t_dict[s[i]] += 1
                            
                    if res_len >= r+1 - l:
                        res_len = r+1 - l
                        res_str = s[l:r+1]
        return res_str