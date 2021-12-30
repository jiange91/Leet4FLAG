class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wc = {}
        for w in words:
            wc[w] = wc.get(w, 0) + 1
        l = len(words[0])
        ans = []
        for i in range(len(s) - l + 1):
            seen, c = {}, 0
            r = i
            while c < len(words) and r < len(s) - l + 1:
                cur = s[r:r+l]
                if cur not in wc:
                    break
                if seen.get(cur, 0) < wc[cur]:
                    seen[cur] = seen.get(cur, 0) + 1
                    r += l
                    c += 1
                else:
                    break
            if c == len(words):
                ans.append(i)
        return ans
                
            
            
            
        # return ans
