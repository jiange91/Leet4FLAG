class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        found = [-1,-1]
        words = [word1, word2]
        res = float('inf')
        if word1 == word2:
            for i in range(len(wordsDict)):
                w = wordsDict[i]
                if w == word1:
                    if found[0] < found[1]:
                        found[0] = i
                    else:
                        found[1] = i
                    if found[0] != -1 and found[1] != -1:
                        res = min(abs(found[0]-found[1]),res)
            return res
        for i in range(len(wordsDict)):
            w = wordsDict[i]
            if w in words:
                found[words.index(w)] = i
            if found[0] != -1 and found[1] != -1:
                res = min(abs(found[0]-found[1]),res)
        return res