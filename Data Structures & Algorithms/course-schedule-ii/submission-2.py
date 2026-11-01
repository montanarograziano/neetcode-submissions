class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visiting:
                return True
            
            
            cycle.add(crs)
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            
            cycle.remove(crs)
            visiting.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

