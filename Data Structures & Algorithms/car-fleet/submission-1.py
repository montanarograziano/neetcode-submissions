class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position, speed = list(zip(*sorted(((p, s) for p, s in zip(position, speed)), key=lambda x: -x[0])))
        res = 0
        cur_time = -1
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            if time > cur_time:
                res += 1
                cur_time = time
        
        return res
