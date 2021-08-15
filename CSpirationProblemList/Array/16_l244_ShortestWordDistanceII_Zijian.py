class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wd = {}
        for i, w in enumerate(wordsDict):
            self.wd[w] = self.wd.get(w, []) + [i]
                        

    def shortest(self, word1: str, word2: str) -> int:
        is1, is2 = self.wd[word1], self.wd[word2]
        i, j = 0, 0
        ans = float('inf')
        while i < len(is1) and j < len(is2):
            ans = min(ans, abs(is1[i] - is2[j]))
            if is1[i] < is2[j]:
                i += 1
            else:
                j += 1
        return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
