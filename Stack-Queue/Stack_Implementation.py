# STACK 
# LAST IN FIRST OUT 

# Implementation Using Linked_List

class Node : 
    def __init__ (self,elem,next=None) :
        self.elem = elem
        self.next = None

class LL_Stack :
    def __init__ (self) :
        self.top = None
    
    def pop (self) :
        if self.top == None : 
            print("Stack Underflow !!!")
        else : 
            rm = self.top 
            self.top = self.top.next
            rm.next = None
            return rm.elem
    
    def push (self,elem) :
        new = Node(elem)
        new.next = self.top
        self.top = new
    
    def isEmpty (self) :
        if self.top  : 
            return False
        else : 
            return True
    
    def peek (self) :
        return self.top.elem
    
    def delete (self) :
        while self.top  : 
            temp = self.top 
            self.top = self.top.next
            temp.next = None
        print("Stack Deleted !")



# Implementation Using Array 

import numpy as np

class Ar_Stack : 
    def __init__ (self,capacity) :
        self.stack = np.array([None]*capacity)               
        self.top = 0 
        self.size = 0 
    
    def push (self,elem) :
        if self.size == len(self.stack) :
            print("Stack Overfow !!!")
        else : 
            self.stack[self.top] = elem
            self.top += 1 
            self.size += 1 
    
    def pop (self) :
        if self.size == 0 : 
            print("Stack Underflow !!!")
        else : 
            rm = self.stack[self.top-1]
            self.stack[self.top-1] = None
            self.top -= 1
            self.size -= 1
            return rm
    
    def isEmpty (self) :
        if self.size == 0 : 
            return True
        return False
    
    def peek (self) :
        if self.size == 0 : 
            print("Stack Underflow !!!")
        else : 
            return self.stack[self.top-1]
    
    def delete (self) :
        self.stack[:] = None
        self.top = 0 
        self.size = 0 
        print("Stack Deleted !")








