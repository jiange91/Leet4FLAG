from sortedcontainers import SortedSet

class SummaryRanges:
    
    def __init__(self):
        self.ss = SortedSet()
        self.map = {}
        
    def addNum(self, val: int) -> None:
        ss, m = self.ss, self.map
        pos = ss.bisect_right(val)
        prev = ss[pos - 1] if pos > 0 else None
        nex = ss[pos] if pos < len(ss) else None
        if prev is not None and m[prev][0] <= val and m[prev][1] >= val:
            return

        if prev != None and nex != None and val == m[prev][1] + 1 and val == m[nex][0] - 1:
            m[prev] = (m[prev][0], m[nex][1])
            del m[nex]
            ss.remove(nex)

        elif prev is not None and val == m[prev][1] + 1:
            m[prev] = (m[prev][0], val)

        elif nex != None and val == m[nex][0] - 1:
            m[val] = (val, m[nex][1])
            ss.remove(nex)
            del m[nex]
            ss.add(val)

        else:
            ss.add(val)
            m[val] = (val, val)
    
    def getIntervals(self) -> List[List[int]]:
        res = []
        for val in self.ss:
            res.append([self.map[val][0], self.map[val][1]])
        return res