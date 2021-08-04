class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        degree = {}
        chars = set(''.join(words))
        for c in chars:
            degree[c] = 0
            graph[c] = set()
        for w1, w2 in zip(words, words[1:]):
            i = 0
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        degree[c2] += 1
                    break
                i += 1
            if i == len(w2) and len(w1) > len(w2): return ""
        q = collections.deque(c for c in chars if not degree[c])
        ord = []
        while q:
            smaller = q.popleft()
            ord.append(smaller)
            for c in graph[smaller]:
                degree[c] -= 1
                if not degree[c]:
                    q.append(c)
        return "" if len(ord) != len(degree) else ''.join(ord)
        
        
