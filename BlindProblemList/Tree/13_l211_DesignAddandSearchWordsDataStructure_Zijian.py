class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.rel = False

    def addWord(self, word: str) -> None:
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t[';'] = {}

    def dfs(self, word, t):
        if not word:
            if ';' in t:
                self.rel = True
            return
        if word[0] == '.':
            for v in t.values():
                self.dfs(word[1:], v)
        elif word[0] not in t:
                return
        else:
            self.dfs(word[1:], t[word[0]])
            
        
    def search(self, word: str) -> bool:
        self.rel = False
        self.dfs(word, self.trie)
        return self.rel


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
