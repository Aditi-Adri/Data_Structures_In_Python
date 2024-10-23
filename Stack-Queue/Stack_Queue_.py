
###                 Use a single list to implement 3 stacks                        ###

class Multi_Stack :
    def __init__ (self,per_stack_size) :
          self.stack_num = 3
          self.List = [0] * (self.stack_num * per_stack_size)
          self.per_stack = [0] * self.stack_num
          self.stack_size = per_stack_size
    
    def is_full (self,stack_num) :
         return  self.per_stack[stack_num] == self.stack_size
    def is_Empty (self,stack_num) :
         return self.per_stack[stack_num] == 0 
    
    def top_index (self,stack_num) :
         x = stack_num * self.stack_size
         return x + self.per_stack[stack_num] - 1
    
    def push (self,item,stack_num) :
         if self.is_full (stack_num) :
              return "Stack overflow !!"
         else : 
              self.per_stack[stack_num] += 1 
              self.List[self.top_index(stack_num)] = item
    
    def pop (self,stack_num) :
         if self.is_Empty (stack_num) :
              return "Stack underflow !!"
         else : 
              rm = self.List[self.top_index(stack_num)]
              self.List[self.top_index(stack_num)] = 0 
              self.per_stack[stack_num] -= 1
              return rm
    
    def peek (self,stack_num) :
         if self.is_Empty(stack_num) : 
              return "Stack is Empty"
         else : 
              return self.List[self.top_index(stack_num)]


st = Multi_Stack (6)
st.is_full(0)
st.push(9,1)
st.push(4,1)
print(st.peek(1))




####                   create Stack for returning the min value           ###


class Node : 
     def __init__ (self,elem,next=None) :
          self.elem = elem
          self.next = next
    
class Stack :
    def __init__ (self) :
          self.top = None
          self.min = None
    
    def min_val (self) :
         if self.min : 
              return self.min.elem
         return None
    
    def push (self,val) :
         if self.min and self.min.elem < val : 
              self.min = self.min
         else : 
              self.min = Node(val,self.min)
         self.top = Node(val,self.top)
    
    def pop (self) :
         if self.top == None :
              return None
         rm = self.top.elem
         self.top = self.top.next
         return rm


c1 = Stack()
c1.push(5)
print(c1.min_val())
c1.push(0)
print(c1.min_val())



###                      Stack Of Plates 
# after reaching max capacity , need to create another stack,; but in pop func it should act like single stack


class plate_stack :
    def __init__ (self,capacity) :
          self.cap =  capacity
          self.stack = []
    
    def push (self,elem) :
        if len(self.stack) > 0 and len(self.cap[-1]) < self.cap :
              self.stack[-1].append(elem)
        else :
             self.stack.append(elem)
    
    def pop (self) :
        while len(self.stack) and len(self.stack[-1]) == 0 : 
              self.stack.pop()
        if len(self.stack) == 0 :
             return None
        else : 
             return self.stack[-1].pop()
    
    def pop_at (self,stack_num) :
         if len(self.stack[stack_num]) > 0 : 
              return self.stack[stack_num].pop()
         else :
              return None
    

###                    Implement a queue using two stacks

class stack : 
    def __init__ (self) :
          self.list = []
    
    def push(self, item):
        self.list.append(item)
  
    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()
    
class queue_stack : 
    def __init__ (self) :
          self.st1 = stack()
          self.st2 = stack()
    
    def enqueue (self,item) :
         self.st1.push(item)
    
    def dequeue (self) :
        while len(self.st1) :
            self.st2.push(self.st1.pop())
        rm = self.st2.pop()
        while len(self.st2):
            self.st1.push(self.st2.pop())
        return rm
    
    
              
  

     


        
         

    
