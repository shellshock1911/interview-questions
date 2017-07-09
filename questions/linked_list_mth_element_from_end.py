"""Find the element in a singly linked list that's m elements from the end.

   ** Taken from Udacity Machine Learning Nanodegree Program **
"""

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

def mth_element_from_end(ll, m):
    
    if not ll:
        return None
    
    length = 0
    current = ll.head
    
    while current:
        length += 1
        current = current.next
        
    if m > length:
        return None
    
    current = ll.head
    
    for _ in xrange(length - m):
        current = current.next
    
    return current.data

########################################
# Test Cases
########################################

ll = LinkedList()
print mth_element_from_end(ll, 4)
# Output == None
ll = None
print mth_element_from_end(ll, 6)
# Output == None
a, b, c, d, e, f, g = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)
ll = LinkedList(a)
ll.append(b)
ll.append(c)
ll.append(d)
ll.append(e)
ll.append(f)
ll.append(g)
print mth_element_from_end(ll, 3)
# Output == 5
print mth_element_from_end(ll, 1)
# Output == 7
print mth_element_from_end(ll, 7)
# Output == 1
print mth_element_from_end(ll, 8)
# Output == None
