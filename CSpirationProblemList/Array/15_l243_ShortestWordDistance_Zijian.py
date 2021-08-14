class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        ans = n
        i1, i2 = n, n
        for i in range(n):
            if wordsDict[i] == word1:
                i1 = i
                if i2 >= 0:
                    ans = min(ans, abs(i1-i2))
            elif wordsDict[i] == word2:
                i2 = i
                if i1 >= 0:
                    ans = min(ans, abs(i1-i2))
        return ans
