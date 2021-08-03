class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        table = [0] * len(s)
        table[0] = 1
        for i in range(len(s)):
            if i:
                if int(s[i]) == 0 and (int(s[i-1]) == 1 or int(s[i-1]) == 2):
                    if i - 2 >= 0:
                        table[i] = table[i-2]
                    else:
                        table[i] = 1
                elif int(s[i]) == 0:
                    return 0
                elif int(s[i]) <= 6 and i - 1 >= 0 and int(s[i-1]) == 2:
                    if i - 2 >= 0:
                        table[i] = table[i-1] + table[i-2]
                    else:
                        table[i] = table[i-1] + 1
                elif i - 1 >= 0 and int(s[i-1]) == 1:
                    if i - 2 >= 0:
                        table[i] = table[i-1] + table[i-2]
                    else:
                        table[i] = table[i-1] + 1
                else:
                    table[i] = table[i-1]
        return table[-1]
                    