import sys
sys.path.append('./queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right: 
                # if there is a right node, consider it a root and recurse
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        elif value < self.value:
            if self.left:
                # if there is a left node, consider it a root and recurse
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value and self.right:
            return self.right.contains(target)
        elif target < self.value and self.left:
            return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # iterative way
        # cur=self    
        #  # go  right as far as you can
        # while cur.right is not None:
        #         cur=cur.right
        # return cur.value        
      
        # recursive way

        # base case
        if self.right is None:
            return self.value
        # recursive case
        else:
            return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
    #    calling fun on current node
        cb(self.value)
      # base case
      # 
   
    # recursive case
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb) 
    # base case, no need to return
    # else if both are none ,stop recursion
   
    # def iterative_for_each(self,cb):
    #     if self is None:
    #         return "BST empty"
    #     # Root node
    #     cb(self.value)
    #     # 
    #     # All children
    #     while len(stack)>0:
    #         # poo top of stack
    #         # cb(top of stack)
    #         # if left child ,then push to stack
    #         # if right child ,then push to stack 
             

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # left root right
        # base case

        # recursive case
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
