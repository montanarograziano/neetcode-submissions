class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = list(zip(*sorted(((p, s) for p, s in zip(position, speed)), key=lambda x: -x[0])))
        res = 0
        s = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            if not s or time > s[-1]:
                s.append(time)
        
        return len(s)
