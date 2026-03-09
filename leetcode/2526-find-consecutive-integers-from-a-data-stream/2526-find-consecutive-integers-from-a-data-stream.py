from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.length = [0,k]#[current,max]

    def consec(self, num: int) -> bool:
       
        if self.length[0] < self.length[1]-1:
            if num == self.val:
                self.length[0] += 1
            else:
                self.length[0] = 0
            return False
        else:
            if num == self.val:
               
                return True
            else:
                
                self.length[0] = 0
                return False
        
        