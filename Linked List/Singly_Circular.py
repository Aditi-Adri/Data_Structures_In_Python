# Non Dummy headed 

# Singly Circular Linked list 

class Node : 
    def __init__ (self,elem,next=None) :
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
    temp.next = head
    return head

# print Linked List
def display (head) :
    if head :
        temp = head
        print(temp.elem,end="-->")
        temp = temp.next
        while temp != head : 
            print(temp.elem,end= "-->")
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
    if ind < 0 or ind > count(head) :
        return head                      # Invalid index
    elif ind == 0 : 
        new = Node(elem,head)
        temp = head.next
        while temp.next != head :
            temp = temp.next
        temp.next = new
        return new
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
        new = head.next 
        temp = head.next
        while temp.next != head : 
            temp = temp.next
        temp.next = new
        new.next = None
        return new
    else :
        prv = get_node (head,ind-1)
        rm = prv.next
        prv.next = rm.next
        rm.next = None
        return head

# reverse in place
def reverse_in_place (head) :
    temp = head.next
    new_head = head 
    while temp != head : 
        n = temp.next
        temp.next = new_head
        new_head = temp 
        temp = n 
    head.next = new_head
    return new_head

# reverse out of place 
def reverse_out_of_place (head) :
    new_head = Node(head.elem)
    last = new_head
    temp = head.next
    while temp != head : 
        n = Node(temp.elem,new_head)
        new_head = n 
        temp = temp.next
    last.next = new_head
    return new_head

# right rotate
def rotate_right (head) :
    return head.next

# left rotate
def rotate_left (head) :
    temp = head.next
    while temp.next != head : 
        temp = temp.next
    return temp







