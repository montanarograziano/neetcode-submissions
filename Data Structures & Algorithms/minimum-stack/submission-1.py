class MinStack:

    def __init__(self):
        self.s = []
        self.m =  []
        

    def push(self, val: int) -> None:
        self.s.append(val)
        self.m.append(min(self.m[-1] if self.m else val, val))
        

    def pop(self) -> None:
        self.m.pop()
        self.s.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.m[-1]
        
