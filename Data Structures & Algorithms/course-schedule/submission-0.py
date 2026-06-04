class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0] * numCourses
        cormap = defaultdict(list)
        for src, dst in prerequisites:
            cormap[src].append(dst)
            ind[dst] += 1

        q = deque()
        for i, n in enumerate(ind):
            if n == 0:
                q.append(i)

        finish = 0
        print(q)
        while q:
            cur = q.popleft()
            finish += 1
            for nei in cormap[cur]:
                ind[nei] -= 1
                if ind[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses
