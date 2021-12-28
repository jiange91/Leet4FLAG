class Solution:
    def maxEnvelopes(self, envs: List[List[int]]) -> int:
        senvs = sorted(envs, key=lambda x: x[1], reverse=True)
        senvs = sorted(senvs, key=lambda x: x[0], reverse=False)
        slots = []
        slots.append(senvs[0][1])
        ans = 1
        for i in range(1, len(senvs)):
            if senvs[i][1] > slots[-1]:
                slots.append(senvs[i][1])
                ans = ans + 1
            else:
                idx = self.bs(slots, senvs[i][1])
                slots[idx] = senvs[i][1]
        return ans
    
    def bs(self, slots, t):
        begin, end = 0, len(slots) - 1
        while begin < end:
            m = begin + (end - begin) // 2
            if slots[m] < t:
                begin = m + 1
            else:
                end = m
        return begin
        # g = {}
        # n = len(envs)
        # for i in range(n):
        #     g[i] = []
        # for i in range(n):
        #     for j in range(i, n):
        #         if envs[i][0] > envs[j][0] and envs[i][1] > envs[j][1]:
        #             g[i].append(j)
        #         elif envs[i][0] < envs[j][0] and envs[i][1] < envs[j][1]:
        #             g[j].append(i)
        # # print(g)
        # visited = [False] * n
        # dps = [1] * n
        # for i in range(n):
        #     if not visited[i]:
        #         self.traverse(g, i, visited, dps)
        # ans = 0
        # # print(dps)
        # for i in dps:
        #     ans = max(ans, i)
        # return ans
        
    def traverse(self, g, start, visited, dps):
        visited[start] = True
        for i in range(len(g[start])):
            if not visited[g[start][i]]:
                self.traverse(g, g[start][i], visited, dps)
            # print("{},{},{}".format(i, dps[i], dps[g[start][i]]))
            dps[start] = max(dps[start], 1 + dps[g[start][i]])

