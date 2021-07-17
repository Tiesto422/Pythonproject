class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


head = LinkedList(0)
currentNode = head
for i in range(1, 10):
    node = LinkedList(i)
    currentNode.next = node
    currentNode = currentNode.next

currentNode = head
while currentNode != None:
    print(currentNode.value)
    currentNode = currentNode.next
