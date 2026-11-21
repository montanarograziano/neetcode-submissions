class Solution:
    def foreignDictionary(self, words):
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
            
        
        # now khan
        q = deque([c for c in indegree if indegree[c] == 0])
        res = ""
        while q:
            cur = q.popleft()
            res += cur
            for dst in adj[cur]:
                indegree[dst] -= 1
                if indegree[dst] == 0:
                    q.append(dst)
        
        return res if len(indegree) == len(res) else ""
        
            


