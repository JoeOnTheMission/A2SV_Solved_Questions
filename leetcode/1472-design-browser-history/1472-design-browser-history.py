class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        # create node  
        self.head = Node(None)
        self.tail = Node(None)
        self.home = Node(homepage)
        # connect node
        self.head.next = self.home
        self.home.prev = self.head 
        self.home.next = self.tail
        self.tail.prev = self.home 
        # current page
        self.cur = self.home

    def visit(self, url: str) -> None:
        #update pointers
        page = Node(url)
        # cut off forward history
        self.cur.next = self.tail
        self.tail.prev = self.cur

        # connect new page
        self.cur.next = page
        page.prev = self.cur
        page.next = self.tail
        self.tail.prev = page

        self.cur = page
    def back(self, steps: int) -> str:
        while self.cur.prev != self.head and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.value


    def forward(self, steps: int) -> str:
        while self.cur.next != self.tail and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.value


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)