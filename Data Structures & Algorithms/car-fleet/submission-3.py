class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        t = sorted(zip(position, speed), key= lambda x: -x[0])
        for p, s in t:
            time = (target - p) / s
            if fleets and fleets[-1] >= time:
                continue
            fleets.append(time)
        
        return len(fleets)