"""
Implementation of DoublyLinkedList
"""
class Node:
    def __init__(self, val=0, prev=None, next=None) -> None:
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self, head=None, tail=None) -> None:
        self.length = 0
        self.head = head
        self.tail = tail

    def prepend(self, item):
        node = Node(val=item)
        self.length += 1
        if not self.head:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_at(self, item, idx):
        if idx > self.length:
            raise Exception("out of bounds")
        
        if idx == self.length:
            self.append(item)
            return
        elif idx == 0:
            self.prepend(item)
        
        self.length += 1
        curr = self.head

        i = 0
        while curr and i < idx:
            curr = curr.next
        node = Node(val=item)
        node.next = curr
        node.prev = curr.prev
        curr.prev = node

        if node.prev:
            node.prev.next = curr
        pass

    def append(self, item):
        self.length += 1
        node = Node(val=item)
        if not self.head:
            self.head = self.tail = node
            return
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def remove(self, item):
        curr = self.head
        for _ in range(0,self.length):
            if curr.val == item:
                break
            curr = curr.next

        if not curr:
            return -1
        
        self.length -= 1

        if self.length == 0:
            value = self.head.val
            self.head = self.tail = None
            return value
        
        prev = curr.prev
        next = curr.next

        if prev:
            prev.next = next
        
        if next:
            next.prev = prev

        if curr == self.head:
            self.head = curr.next
        
        if curr == self.tail:
            self.tail = curr.prev

        curr.prev = curr.next = None
        return curr.val

    def get(self, idx):
        pass

    def _get_at(self, idx):
        pass

    def remove_at(self,idx):
        pass
    
    def size(self):
        return self.length

