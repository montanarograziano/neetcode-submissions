class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        boats = []
        l, r = 0, len(people) - 1
        # 1, 2, 2, 3, 3
        # 3 - 3 - 1,2 - 2
        while l <= r:
            a, b = people[l], people[r]
            cur = []
            if a + b <= limit:
                boats.append([a, b])
                l, r = l + 1, r - 1
            else:
                boats.append(b)
                r -= 1
            res += 1
        
        return res
