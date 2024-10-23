# QUEUE
# FIRST IN FIRST OUT 

# Implementation using circular Array 

class Node : 
    def __init__ (self,capacity) :
        self.queue = [None]*capacity
        self.front = self.back = 0 
    
    def enqueue (self,elem) :
        if self.queue[self.back] != None : 
            print("at Full capacity.Cannot enqueue")
        else : 
            self.queue[self.back] = elem
            self.back = ( self.back + 1 ) % len(self.queue)
    
    def dequeue (self) :
        if self.queue[self.front] == None : 
            print("queue is empty. Cannot dequeue.")
        else : 
            rm = self.queue[self.front]
            self.queue[self.front] = None
            self.front =  ( self.front + 1 ) % len(self.queue)
            return rm
    
    def isEmpty (self) :
        return self.queue[self.front] == None
    
    def printQueue(self):
            i=self.front
            print(self.queue[i],end=' | ')
            i=(i+1)%self.queue.size
            while i!=self.back:
                print(self.queue[i],end=' | ')
                i=(i+1)%self.queue.size
            print()


# Implementation using singly linked list

class Node : 
    def __init__ (self,elem,next = None) :
        self.elem = elem
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode
    
    def isEmpty(self):
        return self.linkedList.head == None
    
    def peek(self):
        if self.isEmpty():
            return "No node in the queue"
        else:
            return self.linkedList.head
    
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


