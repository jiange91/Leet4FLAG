class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        i1, i2 = n, n
        ans = n
        for i in range(n):
            if wordsDict[i] == word1:
                if word1 == word2:
                    if i1 >= n:
                        i1 = i
                    elif i2 >= n:
                        i2 = i
                    elif i1 < i2:
                        i1 = i
                    else:
                        i2 = i
                else:
                    i1 = i
                ans = min(ans, abs(i1-i2))
            elif wordsDict[i] == word2:
                i2 = i
                ans = min(ans, abs(i1-i2))
        return ans
