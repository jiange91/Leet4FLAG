# class TrieNode:
#     def __init__(self):
#         self.next = {}
#         self.ps = []
        

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d = {}
        for i, w in enumerate(words):
            d[w] = i
        ans = []
        for i, w in enumerate(words):
            if w[::-1] in d and d[w[::-1]] != i:
                ans.append([i, d[w[::-1]]])
            if w == w[::-1] and w != '' and '' in d:
                ans.append([i, d['']])
                ans.append([d[''], i])
            for k in range(1, len(w)):
                s1, s2 = w[:k], w[k:]
                if s1 == s1[::-1] and s2[::-1] in d:
                    ans.append([d[s2[::-1]], i])
                if s2 == s2[::-1] and s1[::-1] in d:
                    ans.append([i, d[s1[::-1]]])
        return ans
                    
