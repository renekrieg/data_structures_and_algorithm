class NewNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    def __str__(self):
        return f'{{value: {self.value}, next: {self.next}}}'
    

class LinkedList:
    def __init__(self, value; None):
        head = NewNode(value)
        self.head = head
        self.tail = self.head
        self.length = 1    
    
    def __str__(self):
        return f'head: {self.head}, tail: {self.tail} length: {self.length}'
    
    def append(self, value):
        tail = NewNode(value)
        self.tail.next = tail
        self.tail = tail
        self.length += 1
        return tail
    
    def prepend(self, value,):
        head = NewNode(value)
        self.head = head
        self.length +=1
        return head
        
        
        
myLinkedList = LinkedList(10);
print(myLinkedList)
print(myLinkedList.append(5))
print(myLinkedList)
print(myLinkedList.prepend(100))
print(myLinkedList)