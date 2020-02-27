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
        # store the refrence to  old next in current_next bcoz we will overwrite it later
        current_next = self.next
        # create a new node with next pointer current_next 
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
        if self.length==0: #linked list is empty
            newNode = ListNode(value,None,None)
            self.head=newNode
            self.tail=newNode
            self.length+=1
        elif self.length>0: 
            # create the node and insert before the current head   
            self.head.insert_before(value)
            # update the new node as new head ie update self.head
            self.head=self.head.prev #newhead is old head's previous pointer
            # tail doesn't change when head is added or removed
            self.length+=1
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.length==0:
            head_value = None
        elif self.length==1:
            head_value = self.head.value
            self.head=None
            self.tail=None
            self.length=0
        elif self.length>1:
            head_value = self.head.value
            cur_head=self.head.next
            self.head.delete()
            self.head=cur_head #new head is now old heads next pointer
            # tail doesn't change when head is added or removed
            self.length-=1
        return head_value
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.length==0: #linked list is empty
            newNode = ListNode(value,None,None)
            self.head=newNode
            self.tail=newNode
            self.length+=1
        elif self.length>0: 
            # create the node and insert after the current tail
            self.tail.insert_after(value)
            # update the new node as new tail ie update self.tail
            # head doesn't change when tail is added or removed
            self.tail=self.tail.next
            self.length+=1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.length==0:
            tail_value = None
        elif self.length==1:
            tail_value = self.tail.value
            self.head=None
            self.tail=None
            self.length=0 
        elif self.length>1:
            tail_value = self.tail.value
            new_tail=self.tail.prev
            self.tail.delete()
            # head doesn't change when tail is added or removed
            self.tail=new_tail
            self.length-=1
        return tail_value
        
    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # length does not chnage in this case  
        if node != self.head:
            # remove
            self.delete(node)
            # insert @ head
            self.add_to_head(node.value)
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node != self.tail: #only do this if node is not at the tail
             # remove
            self.delete(node)
            # insert @ tail
            self.add_to_tail(node.value)


    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not self.head and not self.tail:  #LL is empty
            return "Error"
        elif self.head==self.tail==node: #deleting from list of one node
            self.head=None
            self.tail=None
        elif self.head==node: # node is head 
            self.head=node.next 
        elif self.tail==node:  # node is tail
            self.tail=node.prev
        self.length-=1
        node.delete()
     
    """Returns the highest value currently in the list"""
    def get_max(self):
        max_value = self.head.value if self.head else None
        current=self.head
        while(current):
            max_value = current.value if current.value>max_value else max_value
            current=current.next
        return max_value
