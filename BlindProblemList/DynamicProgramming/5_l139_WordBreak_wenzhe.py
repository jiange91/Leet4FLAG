class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    
        self.currentEnds = set()
        self.currentEnds.add(0)
        
        return self.wordContain(s, 0, wordDict)
    
    def wordContain(self, s, i, wordDict):
        if i == len(s):
            return True
        ends = []
        
        for word in wordDict:
            if(len(s) - len(word) - i >= 0 and s[i:len(word)+i] == word):
                if not i + len(word) in self.currentEnds:
                    ends.append(i + len(word))
                    self.currentEnds.add(i+len(word))
        if ends == []:
            return False
        for i in ends:
            if self.wordContain(s, i, wordDict):
                return True
        return False