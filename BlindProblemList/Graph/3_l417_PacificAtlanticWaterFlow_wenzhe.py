class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res_p = [[False for _ in heights[0]] for _ in heights]
        res_a = [[False for _ in heights[0]] for _ in heights]

        expanded = set()
        visited = set()
        frontier = set()
        for i in range(len(heights)):
            res_p[i][0] = True
            visited.add((i,0))
            frontier.add((i,0))
        for i in range(len(heights[0])):
            res_p[0][i] = True
            visited.add((0,i))
            frontier.add((0,i))

        while len(frontier) != 0:
            newFrontier = set()
            for (i,j) in frontier:
                expanded.add((i,j))
                if i!=0 and heights[i-1][j] >= heights[i][j] and (i-1,j) not in visited:
                    newFrontier.add((i-1,j))
                    visited.add((i-1,j))
                    res_p[i-1][j] = True
                if i!=len(heights)-1 and heights[i+1][j] >= heights[i][j] and (i+1,j) not in visited:
                    newFrontier.add((i+1,j))
                    visited.add((i+1,j))
                    res_p[i+1][j] = True
                if j!=0 and heights[i][j-1] >= heights[i][j] and (i,j-1) not in visited:
                    newFrontier.add((i,j-1))
                    visited.add((i,j-1))
                    res_p[i][j-1] = True
                if j!=len(heights[0])-1 and heights[i][j+1] >= heights[i][j] and (i,j+1) not in visited:
                    newFrontier.add((i,j+1))
                    visited.add((i,j+1))
                    res_p[i][j+1] = True
            frontier = newFrontier
        expanded = set()
        visited = set()
        frontier = set()
        for i in range(len(heights)):
            res_a[i][-1] = True
            visited.add((i,len(heights[0])-1))
            frontier.add((i,len(heights[0])-1))

        for i in range(len(heights[0])):
            res_a[-1][i] = True
            visited.add((len(heights)-1,i))
            frontier.add((len(heights)-1,i))


            
        while len(frontier) != 0:
            newFrontier = set()
            for (i,j) in frontier:
                expanded.add((i,j))
                if i!=0 and heights[i-1][j] >= heights[i][j] and (i-1,j) not in visited:
                    newFrontier.add((i-1,j))
                    visited.add((i-1,j))
                    res_a[i-1][j] = True
                if i!=len(heights)-1 and heights[i+1][j] >= heights[i][j] and (i+1,j) not in visited:
                    newFrontier.add((i+1,j))
                    visited.add((i+1,j))
                    res_a[i+1][j] = True
                if j!=0 and heights[i][j-1] >= heights[i][j] and (i,j-1) not in visited:
                    newFrontier.add((i,j-1))
                    visited.add((i,j-1))
                    res_a[i][j-1] = True
                if j!=len(heights[0])-1 and heights[i][j+1] >= heights[i][j] and (i,j+1) not in visited:
                    newFrontier.add((i,j+1))
                    visited.add((i,j+1))
                    res_a[i][j+1] = True
            frontier = newFrontier

        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if res_a[i][j] and res_p[i][j]:
                    res.append([i,j])
        return res