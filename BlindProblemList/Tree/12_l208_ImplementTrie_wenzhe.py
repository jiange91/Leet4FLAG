class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        for i in range(ord('a'), ord('z')+1):
            self.root[chr(i)] = [False, None]

    def insert(self, word: str) -> None:
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
        """
        Returns if the word is in the trie.
        """
        cur_root = self.root
        for c in word[:-1]:
            if cur_root[c][1] == None:
                return False
            cur_root = cur_root[c][1]
        return cur_root[word[-1]][0]
    
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
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)