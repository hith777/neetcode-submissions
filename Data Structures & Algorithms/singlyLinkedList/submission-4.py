class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next

        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1    
            curr = curr.next
        
        return -1

    def insertHead(self, val: int) -> None:
        if self.head.next:
            new_node = ListNode(val, self.head.next)
            self.head.next = new_node
        else:
            self.tail = self.head.next = ListNode(val)

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head.next:
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            self.head.next = new_node
            self.tail = new_node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        while i < index and curr:
            curr = curr.next
            i += 1
        
        if curr and curr.next:
            if self.tail == curr.next:
                self.tail = curr
            curr.next = curr.next.next
            return True
        
        return False
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res
        
