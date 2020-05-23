class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
    # reference to the head of the list(If head= None, LL is empty)
        self.head= None
    # reference to the tail of the list
        self.tail= None
    
    def add_to_head(self, value):
        #1. Create new Node with value(to add it to head !)
        new_node=Node(value)
        #2. update the pointer of new Node to --> old head(bcoz we are adding to head)
        new_node.set_next(self.head)
        #3.  mark  new Node as 'head'
        
        # 3a. If we start with an empty LL ie Head=Tail is empty and insert to that
        # i.e. inserting to an empty LL
        if self.head is None:
            # mark new node as head and 'tail' (bcoz 1st element has node with head=tail)
            self.head=new_node
            self.tail=new_node
        # 3b. Inserting into list with one or more nodes
        else:
            self.head=new_node
            # tail will be unaffected  in this case



        
       
    
    def add_to_tail(self, value):
        #1. Create new Node with value(to add it to tail !)
        new_node = Node(value)
         #2.We don't need to update the next pointer of new Node (bcoz we are adding to tail) and with an 
         #  empty list it is initialised to None,  self.tail= None in line 24
         # i.e. inserting to an empty LL

        #2. update next pointer of old 'tail'(if list is not empty)
        new_node.set_next(self.tail)
        # inserting  into empty LL
        if self.tail  is None:
            # mark new node as 'head' and tail (bcoz 1st element has node with head=tail)
            self.head=new_node
            self.tail=new_node
        # inserting  into  LL with one or more nodes   
        else:
            self.tail=new_node    
    
    def remove_head(self):
        # REMOVE FROM EMPTY LL
        if self.head is None:
            return "Error"
        # REMOVE FROM LL with 1 element ie head= tail
        elif self.head==self.tail:  
            self.head=None
            self.tail=None
        # general
        else:
            # new head is old head's next Node
            self.head=self.head.get_next()
    
    
    
    # STRETCH
    def insert_at(self, value, position):
        pass
    def contains(self, value):
        # temparory pointer which always starts from head
        cur_node=self.head
        while(cur_node is not None):
            # ie there is at least one node after it
            cur_node =cur_node .get_next()
