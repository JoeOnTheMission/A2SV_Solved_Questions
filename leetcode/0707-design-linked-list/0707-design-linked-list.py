
class Node:
    def __init__(self,value):
        self.val = value
        self.next = None

"""
dummy 1 2 3 4 5 
      0 1 2 3 4
"""

class MyLinkedList:

    def __init__(self):
        #dummy head 
        self.head = Node(None)        

    def get(self, index: int) -> int:
        cur = self.head.next    
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            return cur.val 
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        cur = self.head.next
        if cur:#we have a value at first
            self.head.next = node
            node.next = cur
        else:
            self.head.next = node

        """ def see_linked_list(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next"""

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        prev = self.head
        cur = self.head.next
        while cur:
            cur = cur.next
            prev = prev.next
        prev.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        prev = self.head
        cur = self.head.next
        while cur and index > 0:
            prev = prev.next
            cur = cur.next

            index -= 1
        if index == 0:
            prev.next = node
            node.next = cur
    def deleteAtIndex(self, index: int) -> None:
        if not self.head.next:
            return
        prev = self.head
        cur = self.head.next
        while cur.next and index > 0:
            prev = prev.next
            cur = cur.next
            index -= 1
        if index == 0:
            prev.next = cur.next
    

"""
# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)""
obj.addAtHead(9)
obj.addAtHead(1)
obj.addAtHead(3)
obj.addAtTail(2)
obj.see_linked_list()
obj.deleteAtIndex(0)
obj.see_linked_list()"""