class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ""
        for s in strs:
            ans = ans + str(len(s)) + '#' + s
        # print(ans)
        return ans

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i = 0
        ans = []
        while i < len(s):
            j = i + 1
            while j < len(s) and s[j] != '#':
                j = j + 1
            ans.append(s[i+1+len(s[i:j]):i+1+len(s[i:j])+int(s[i:j])])
            i = i + int(s[i:j]) + 1 + len(s[i:j])
        return ans


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
