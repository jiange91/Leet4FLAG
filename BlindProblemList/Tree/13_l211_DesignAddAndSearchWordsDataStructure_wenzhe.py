class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        for i in range(ord('a'), ord('z')+1):
            self.root[chr(i)] = [False, None]

    def addWord(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_root = self.root
        for c in word[:-1]:
            if cur_root[c][1] == None:
                cur_root[c][1] = dict()
                for i in range(ord('a'), ord('z')+1):
                    cur_root[c][1][chr(i)] = [False, None]
            cur_root = cur_root[c][1]
        cur_root[word[-1]][0] = True

    def search(self, word: str) -> bool:
        frontier = [self.root]
        for c in word[:-1]:
            next_frontier = []
            for f in frontier:
                if c == '.':
                    for k in f.keys():
                        if f[k][1] != None:
                            next_frontier.append(f[k][1])
                elif f[c][1] != None:
                    next_frontier.append(f[c][1])
            frontier = next_frontier
        if len(frontier) == 0:
            return False
        if word[-1] == '.':
            res = []
            for i in range(ord('a'), ord('z')+1):
                char = chr(i)
                res.append(any([f[char][0] for f in frontier]))
            return any(res)
        return any([f[word[-1]][0] for f in frontier])
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_root = self.root
        for c in prefix[:-1]:
            if cur_root[c][1] == None:
                return False
            cur_root = cur_root[c][1]
        return cur_root[prefix[-1]][0] or cur_root[prefix[-1]][1]
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)