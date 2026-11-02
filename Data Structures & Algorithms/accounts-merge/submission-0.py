class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if rb > ra:
            ra, rb = rb, ra
        
        self.parent[rb] = ra
        self.rank[ra] += self.rank[rb]

        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        uf = UF(len(accounts))
        email_to_acc = {} # email -> index of acc
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in email_to_acc:
                    uf.union(i, email_to_acc[e])
                else:
                    email_to_acc[e] = i
        
        emailGroup = defaultdict(list) # index of acc - > list of emails
        for e, i in email_to_acc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        
        return res
