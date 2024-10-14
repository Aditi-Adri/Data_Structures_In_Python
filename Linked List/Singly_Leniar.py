# Non Dummy headed 

# Singly Leniar Linked list 

class Node : 
    def __init__ (self,elem,next = None) :
        self.elem = elem
        self.next = next

# array to linked List
def ar_2_LL (ar) :
    head = Node(ar[0])
    temp = head
    for i in range (1,len(ar)) :
        new = Node(ar[i])
        temp.next = new
        temp = new
    return head

# print Linked List
def display (head) :
    temp = head
    while temp  : 
        if temp.next  : 
            print(temp.elem,end= "-->")
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
    if ind < 0 or ind > count(head) :
        return head                      # Invalid index
    elif ind == 0 : 
        new = Node(elem)
        new.next = head
        head = new
        return head
    else : 
        new = Node(elem)
        prv = get_node (head,ind-1)
        nxt = prv.next
        prv.next = new
        new.next = nxt
        return head

# remove
def remove (head,ind) :
    if ind < 0 or ind >= count(head) :
        return head                                # Invalid
    elif ind == 0 : 
        rm = head
        head = head.next 
        rm.next = None
        return head
    else :
        prv = get_node (head,ind-1)
        rm = prv.next
        prv.next = rm.next
        rm.next = None
        return head

# check if element exists 
def contains(head, elem):
  temp = head
  while temp != None:
    if elem == temp.elem:
      return True
    temp = temp.next
  return False

# reverse out of place 
def reverse_out_of_place (head) :
    new_head = Node(head.elem)
    temp = head.next
    while temp : 
        n = Node(temp.elem,new_head)
        new_head = n 
        temp = temp.next
    return new_head

# reverse in place
def reverse_in_place (head) :
    new_head = None
    temp = head 
    while temp : 
        n = temp.next
        temp.next = None
        new_head = temp 
        temp = n 
    return new_head

# left rotate
def rotate_left (head) :
    new_head = head.next
    temp = new_head
    while temp.next :
        temp = temp.next
        temp.next = head
        head.next = None
        head = new_head
        return head

# right rotate
def rotate_right (head) :
    last_node = head.next
    second_last_node = head.next
    while last_node.next :
        last_node = last_node.next
        second_last_node = second_last_node.next
    last_node.next = head
    second_last_node.next = None
    head = last_node
    return head

# max elem of LL 
def max_elem (head) :
    temp = head
    max = temp.elem
    while temp : 
        if temp.elem > max : 
            max = temp.elem
        temp = temp.next
    return max

# min elem of LL 
def max_elem (head) :
    temp = head
    min = temp.elem
    while temp : 
        if temp.elem < min : 
            min = temp.elem
        temp = temp.next
    return min

# copy of the current LL
def copy (head) :
    temp = head
    new_head = tail = None
    while temp : 
        n = Node(temp.elem)
        if new_head == None : 
            new_head = n
            tail = new_head
        else : 
            tail.next = n
            tail = tail.next
        temp = temp.next
    return new_head


# Singly Leniar Linked list 


