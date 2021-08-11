class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join('%d:%s' % (len(s), s) for s in strs)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        ans = []
        j = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + int(s[i:j]) + 1
            ans.append(s[j+1:i])
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
