import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
      # Create a new root using the given value and check against the current tree
      new_leaf = BinarySearchTree(value)
      # If the value is >= the current spot move to the right and add it to the right if the field is empty
      if value >= self.value and self.right is None:
        self.right = new_leaf
      elif value >= self.value:
        self.right.insert(value)
      # If the value is < the current spot move to the left and add it to the left if the field is empty
      elif value < self.value and self.left is None:
        self.left = new_leaf
      elif value < self.value:
        self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
      # Check if the current value is equal to the target
      if self.value == target:
        return True
      # Check if the left is equal to the target
      elif target < self.value and self.left is None:
        return False
      elif target < self.value and self.left != target:
        return self.left.contains(target)
      # Check if the right is equal to target
      elif target >= self.value and self.right is None:
        return False
      elif target >= self.value and self.right != target:
        return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
      if self.right:
        return self.right.get_max()
      else:
        # print(self.value)
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
      # Go to each value and use the callback function 
      cb(self.value)
      if self.right is not None:
        self.right.for_each(cb)
      if self.left is not None:
        self.left.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
      if node.left:
        node.in_order_print(node.left)
      print(node.value)  
      if node.right:
        node.in_order_print(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
      new_queue = Queue()
      new_queue.enqueue(node)
      while new_queue.size > 0:
        current = new_queue.dequeue()
        print(current.value)
        if current.left:
          new_queue.enqueue(current.left)
        if current.right:
          new_queue.enqueue(current.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
      new_stack = Stack()
      new_stack.push(node)
      while new_stack.size > 0:
        current = new_stack.pop()
        print(current.value)
        if current.left:
          new_stack.push(current.left)
        if current.right:
          new_stack.push(current.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
      new_stack = Stack()
      new_stack.push(node)
      while new_stack.size > 0:
        current = new_stack.pop()
        print(current.value)
        if current.right:
          new_stack.push(current.right)
        if current.left:
          new_stack.push(current.left)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
      if node.left:
        node.post_order_dft(node.left)
      if node.right:
        node.post_order_dft(node.right)
      print(node.value)
