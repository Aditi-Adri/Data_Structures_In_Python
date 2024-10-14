
# Non Dummy headed 

# Doubly Leniar Linked list 

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
    return head

# print Linked List
def display (head) :
    temp = head
    while temp  : 
        if temp.next  : 
            print(temp.elem,end= "<==>")
        else : 
            print(temp.elem)
        temp = temp.next

# get Node
def get_node (head,ind) :
    temp = head
    cnt = 0 
    while temp : 
        if cnt == ind : 
            return temp
        cnt += 1 
        temp = temp.next
    return "Not Found"

# length
def count (head) :
    temp = head
    cnt = 0 
    while temp : 
        cnt += 1
        temp = temp.next
    return cnt

# get index of a node
def index (head,elem) :
    temp = head
    cnt = 0 
    while temp : 
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
  if ind == 0 :
        new.next = head
        head.prev = new
        head = new
        return head
  elif ind == count(head) :
        prev = get_node (head,ind-1)
        prev.next = new
        new.prev = prev
        return head
  else :
        prev = get_node (head,ind-1)
        nxt = prev.next
        prev.next = new
        new.prev = prev
        new.next = nxt
        nxt.prev = new
        return head
  
# remove
def remove (head,ind) :
    if ind < 0 or ind >= count(head) :
        return head                                # Invalid
    elif ind == 0 : 
        temp = head.next
        head.next = None
        head = temp
        head.prev = None
        return head
    elif ind == count(head)-1 :
        prev = get_node (head,ind-1)
        rm = prev.next
        rm.prev = prev.next = None
        return head
    else :
        rm = get_node (head,ind)
        prev = rm.prev
        nxt = rm.next
        prev.next = nxt
        nxt.prev = prev
        rm.prev = rm.next = None
        return head

# reverse out of place
def reverse_out_of_place (head) :
    new_head = None
    temp = head
    while temp :
        new = Node(temp.elem)
        if new_head == None :
            new_head = new
        else :
            new.next = new_head
            new_head.prev = new
            new_head = new
            temp = temp.next

    return new_head


# reverse in place 
def reverse_in_place(head):
    temp = None
    cur = head
    while cur :
        temp = cur.prev
        cur.prev = cur.next
        cur.next = temp
        cur = cur.prev
    if temp:
        head = temp.prev  
    return head

# left rotate
def rotate_left(head):
    new_head = head.next  
    new_head.prev = None  
    temp = new_head
    while temp.next:
        temp = temp.next
    temp.next = head  
    head.prev = temp
    head.next = None  
    return new_head

# right rotate
def rotate_right(head):
    temp = head
    while temp.next:
        temp = temp.next
    new_head = temp
    prev = temp.prev
    prev.next = None  
    new_head.prev = None 
    new_head.next = head
    head.prev = new_head
    return new_head




