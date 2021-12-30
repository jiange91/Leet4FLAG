class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        slots = [[(words[0], len(words[0]) + 1)]]
        for i in range(1, len(words)):
            if slots[-1][-1][1] + len(words[i]) > maxWidth:
                slots.append([(words[i], len(words[i]) + 1)])
            else:
                slots[-1].append((words[i], slots[-1][-1][1] + len(words[i]) + 1))
        print(slots)
        ans = []
        for idx, words in enumerate(slots):
            tmp = words[0][0]
            if idx < len(slots) - 1:
                nw = len(words)
                if nw > 1:
                    room = maxWidth - (words[-1][1] - nw)
                    base = room // (nw - 1)
                    shift = room % (nw - 1)
                    for i in range(1, len(words)):
                        if shift > 0:
                            blank = "".join([" " for _ in range(1 + base)])
                            shift -= 1
                        else:
                            blank = "".join([" " for _ in range(base)])
                        tmp = tmp + blank + words[i][0]
                else:
                    pad = maxWidth - len(words[0][0])
                    tmp = tmp + "".join([" " for _ in range(pad)])
            else:
                for i in range(1, len(words)):
                    tmp = tmp + " " + words[i][0]
                pad = maxWidth - words[-1][1] + 1
                tmp = tmp + "".join([" " for _ in range(pad)])
            ans.append(tmp)
        return ans
                
