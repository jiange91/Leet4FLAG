class Solution:
    def alienOrder(self, words: List[str]) -> str:
        greater_map = dict()
        smaller_count = dict()
        frontier = set()
        all_chr = set()
        result = []
        prev_w = ''
        
        for w in words:
            if w != prev_w and len(prev_w) >= len(w) and prev_w[:len(w)] == w:
                return ''
            for i in range(min(len(w),len(prev_w))):
                if w[i] != prev_w[i]:
                    if prev_w[i] not in greater_map:
                        greater_map[prev_w[i]] = set()
                    if w[i] not in smaller_count:
                        smaller_count[w[i]] = 0
                    if w[i] not in greater_map[prev_w[i]]:
                        smaller_count[w[i]] += 1
                    greater_map[prev_w[i]].add(w[i])
                    break
            prev_w = w
        
        for w in words:
            for c in w:
                all_chr.add(c)
                if not c in smaller_count:
                    frontier.add(c)
        while len(frontier) != 0:
            newFrontier = set()
            for f in frontier:
                result.append(f)
                if f in greater_map:
                    for g in greater_map[f]:
                        smaller_count[g] -= 1
                        if smaller_count[g] == 0:
                            newFrontier.add(g)
            frontier = newFrontier
            
        return ''.join(result) if len(result) == len(all_chr) else ''