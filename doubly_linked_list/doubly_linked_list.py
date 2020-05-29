"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""

# DLL doesnot have next and previous But each node has next and previous
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # create new node
        new_node=ListNode(value)
        #  if there is head ie more than 1 element
        if self.head: # ie if dll is pointing a head
            new_node.next=self.head  #point new node's next to previous head
            self.head.prev=new_node  # point previous pointer of the previous head to
            # Make new_node as newhead
            self.head=new_node
        # if there is no head
        else:
            self.head=new_node
            self.tail=new_node
        self.length+=1    
            

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # value of the current head
        value=self.head.value
        # delete the current head
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # create  a new node
        new_node=ListNode(value)
        #  if there is tail ie more than 1 element
        # ie if dll is pointing a tail
        if self.tail :  
            new_node.prev=self.tail  #point new node's prev to previous tail
            self.tail.next=new_node  # point next pointer of the previous tail to new node
            # Make new_node as new tail
            self.tail=new_node
            self.length+=1
        # if there is no head
        else:
            self.tail=new_node
            self.head=new_node
            self.length+=1    

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value=self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        
         if node is self.head:
            return
         else:     
            current_node = node
            node.delete()
            self.length -= 1
            self.add_to_head(current_node.value)


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
       if node is self.tail:
            return
        # If node to be deleted is head , make the next pointer of the node self.head
       if node is self.head:
           node.delete()
           self.length-=1
           self.head=node.next 
           self.add_to_tail(node.value)   
       else: 
            current_node = node
            node.delete()
            self.length -= 1
            self.add_to_tail(current_node.value)


    """Removes a node from the list and handles cases where
     the node was the head or the tail"""
    def delete(self, node):
        # dll is empty
        if not self.head:
            print("Nothing Here")
            return
        # if dll has one node
        if self.head==self.tail:
            self.head=None
            self.tail=None
            self.length-=1
       # At least two node and node we delete is head
        if node==self.head:
            self.head= node.next
            self.head.prev=None
            self.length-=1
        # At least two node and node we delete is tail
        if node==self.tail:
            self.tail= node.prev 
            self.head.next=None
            self.length-=1
        # if node to be deleted is in midlle(ie not head or tail)   
        else:
            node.delete()
            

                  
    """Returns the highest value currently in the list"""
    def get_max(self):
        #  max_value = self.head.value if self.head else None
        # current_node=self.head
        # while(current):
        #     max_value = current.value if current.value>max_value else max_value
        #     current=current.next
        # return max_value
        if self.head == self.tail:
            return self.head.value
        max = 0
        curr_node = self.head

        while True:
            if curr_node.value > max:
                max = curr_node.value
            if curr_node.next == None:
                break
            else:
                curr_node = curr_node.next

        return max
