class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('\n')
            res.append(s)
        return ''.join(res)
    
    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        p = 0
        while p!=len(s):
            start_p = p
            while s[p] != '\n':
                p += 1
            length = int(s[start_p:p])
            p += 1
            res.append(s[p: length+p])
            p = length+p
        return res
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))