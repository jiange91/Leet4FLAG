class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        enabling_map = dict()
        requirement_map = dict()
        
        
        for p in prerequisites:
            if p[1] in enabling_map:
                enabling_map[p[1]].append(p[0])
            else:
                enabling_map[p[1]] = [p[0]]
            
            if p[0] in requirement_map:
                requirement_map[p[0]] += 1
            else:
                requirement_map[p[0]] = 1
        
        starting = []
        for c in range(numCourses):
            if c not in requirement_map:
                starting.append(c)
                
        
        taken_set = set()
        while len(starting) != 0:
            new_starting = []
            for s in starting:
                to_enable = enabling_map.get(s, [])
                for c in to_enable:
                    requirement_map[c] -= 1
                    if requirement_map[c] == 0:
                        new_starting.append(c)
                        requirement_map.pop(c)
            starting = new_starting
        
        return len(requirement_map) == 0