# Non Dummy headed 

# Doubly Circular Linked list 

class Node : 
    def __init__ (self,elem,next=None,prev=None) :
        self.elem = elem
        self.next = next
        self.prev = prev

# array to linked List
def ar_2_LL (ar) :
    head = Node(ar[0])
    temp = head
    for i in range (1,len(ar)) :
        n = Node(ar[i])
        temp.next = n
        n.prev = temp 
        temp = n 
    temp.next = head
    head.prev = temp
    return head

# print Linked List
def display (head) :
  if head :
    temp = head
    print(temp.elem,end="<==>")
    temp = temp.next
    while temp  != head : 
        if temp.next  : 
            print(temp.elem,end= "<==>")
        temp = temp.next
    print()

# get Node
def get_node (head,ind) :
    if ind == 0 :
        return head 
    temp = head.next
    cnt = 1
    while temp != head: 
        if cnt == ind : 
            return temp
        cnt += 1 
        temp = temp.next
    return "Not Found"

# length
def count (head) :
    if head == None : 
        return 0 
    temp = head.next
    cnt = 1
    while temp != head : 
        cnt += 1
        temp = temp.next
    return cnt

# get index of a node
def index (head,elem) :
    if head and head.elem == elem : 
        return 0 
    temp = head.next
    cnt = 1
    while temp != head : 
        if temp.elem == elem : 
            return cnt
        temp = temp.next
        cnt += 1
    return "Not Found"

# Insert
def insert (head,ind,elem) :
  new = Node(elem)
  if ind < 0 or ind > count(head) :
        return head   
  new = Node(elem)
  if ind == 0 : 
      new.next = head
      new.prev = head.prev
      head.prev.next = new
      head.prev = new
      return new
  else : 
      prv = get_node(head,ind-1)
      nxt = prv.next
      prv.next = new
      new.prev = prv
      new.next = nxt
      nxt.prev = new
      return head

# remove 
def remove(head, ind):
    if ind < 0 or ind >= count(head):
        return head  
    if ind == 0:  
        if head.next == head: 
            return None
        new_head = head.next
        new_head.prev = head.prev
        head.prev.next = new_head
        head.next = head.prev = None  
        return new_head
    else : 
        rm = get_node(head, ind) 
        prev = rm.prev
        nxt = rm.next
        prev.next = nxt
        nxt.prev = prev
        rm.next = rm.prev = None  
        return head

# reverse out of place 
def reverse_out_of_place(head):
    if head == None :
        return None
    temp = head.prev  
    new_head = Node(temp.elem)
    new_temp = new_head
    temp = temp.prev  
    while temp != head.prev:  
        new_node = Node(temp.elem)
        new_temp.next = new_node
        new_node.prev = new_temp
        new_temp = new_node
        temp = temp.prev
    new_temp.next = new_head
    new_head.prev = new_temp
    return new_head


# reverse in place 
def reverse_in_place(head):
    if head == None :  
        return None
    temp = head
    new_head = None 
    while True:
        temp.next, temp.prev = temp.prev, temp.next
        new_head = temp  
        temp = temp.prev  
        if temp == head:  
            break
    return new_head


# left rotate
def rotate_left (head) :
    if head == None or head.next == head : 
        return head
    return head.next

# right rotate
def rotate_right (head) :
    if head == None or head.next == head : 
        return head
    return head.prev

