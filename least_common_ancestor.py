"""Find the least common ancestor between two nodes on a binary search tree. 
   The least common ancestor is the farthest node from the root that is an 
   ancestor of both nodes. Function should take in a matrix structured 
   like the one below, where the index of the list is equal to the integer 
   stored in that node and a 1 represents a child node, r is a non-negative 
   integer representing the root, and n1 and n2 are non-negative integers 
   representing the two nodes in no particular order.

   [0, 1, 0, 0, 0],
   [0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0],
   [1, 0, 0, 0, 1],
   [0, 0, 0, 0, 0]]
"""

class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    
    def __init__(self, T, r):
        self.root = TreeNode(r)
        self.tree = T

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = TreeNode(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = TreeNode(new_val)
    
    def build_tree(self):
        self.build_tree_helper(self.root.value, self.tree)
    
    def build_tree_helper(self, index, T):
        indices = [i for i, x in enumerate(T[index]) if x == 1]
        for i in indices:
            self.insert(i)
            self.build_tree_helper(i, T)
    
    def search(self, start, find_val):
        return self.search_helper(start, find_val)
                
    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False

    
def LCA_helper(current, n1, n2):
    
    if current is None:
        return None
    
    if current.value > n1 and current.value  > n2:
        return LCA_helper(current.left, n1, n2)
 
    if current.value < n1 and current.value < n2:
        return LCA_helper(current.right, n1, n2)
    
    return current.value

def LCA(T, r, n1, n2):
    
    if not T or r is None:
        return None
    
    tree = BST(T, r)
    tree.build_tree()
    current = tree.root
    return LCA_helper(current, n1, n2)

########################################
# Test Cases
########################################

T, r, n1, n2 = [], 4, 1, 2
print LCA(T, r, n1, n2)
# Output == None
T = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]
r, n1, n2 = None, 5, 6
print LCA(T, r, n1, n2)
r, n1, n2 = 3, 1, 4
print LCA(T, r, n1, n2)
# Output == 3
T =  [[0,0,0,0,0,0,0,0,0,0,0],
      [1,0,0,0,0,0,0,0,0,0,0],
      [0,1,0,0,1,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,1,0,1,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0],
      [0,0,1,0,0,0,0,1,0,0,0],
      [0,0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,1,0,0,1,0],
      [0,0,0,0,0,0,0,0,0,0,1],
      [0,0,0,0,0,0,0,0,0,0,0]]
r, n1, n2 = 8, 0, 5
print LCA(T, r, n1, n2)
# Output == 2
r, n1, n2 = 8, 5, 0
print LCA(T, r, n1, n2)
# Output == 2
r, n1, n2 = 8, 3, 10
print LCA(T, r, n1, n2)
# Output == 8


    