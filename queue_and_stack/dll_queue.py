import sys
sys.path.append('./doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList(None)
    
    # `enqueue` should add an item to the back of the queue.
    def enqueue(self, value):
        self.storage.add_to_tail(value)
    # removing
    def dequeue(self):
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.length
