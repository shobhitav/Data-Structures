"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


#  array vs DLL
# array: add to back O(1)
# array: add to front O(n)
# array: delete from back O(n)
# array:  delete from front O(n)
# array: join text buffers together O(n)

# DLL: add to back O(1)
# DLL: add to front O(1)
# DLL: delete from back O(1)
# DLL:  delete from front O(1)
# DLL: join text buffers together O(1)

import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        return self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_from_head()
        
