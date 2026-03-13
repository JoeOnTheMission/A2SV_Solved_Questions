class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = deque()
        self.k = k
        self.cur_len = 0
    def insertFront(self, value: int) -> bool:
        if self.k == self.cur_len:
            return False
        self.queue.appendleft(value)
        self.cur_len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.k == self.cur_len:
            return False
        self.queue.append(value)
        self.cur_len += 1
        return True

    def deleteFront(self) -> bool:
        if self.queue:
            self.queue.popleft()
            self.cur_len -= 1
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.queue:
            self.queue.pop()
            self.cur_len -= 1
            return True
        else:
            return False
        
    def getFront(self) -> int:
        if self.queue:
            return self.queue[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.queue:
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.cur_len == 0:
            return True
        return False
        
    def isFull(self) -> bool:
        if self.cur_len == self.k:
            return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()