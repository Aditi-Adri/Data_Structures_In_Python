# Queue
# Modules 

# Collection Module

from collections import deque

q1 = deque (maxlen=3)
print(q1)
q1.append(1)         # Inserts value
q1.append(2)
q1.append(3)
q1.append(4)         # Appending beyond maxLength will dequeu first item
print(q1)

q1.popleft()         # dequeu the first value (FIFO)
print(q1)           
q1.clear()           # full clear queue
print(q1)

print("*888888888888888888")
# Queue Module

import queue as q 

q1 = q.Queue(maxsize=3)
print(q1.empty())
q1.put(1)            # enqueue
q1.put(2)
q1.put(3)             # appending more elem than maxlen will create not excecution
print(q1)             # adress
print(q1.get())          # dequeu
print(q1.full())
print(q1.qsize())


# multiprocessing module

from multiprocessing import Queue

q1 = Queue(maxsize= 3)
q1.put(1)
print(q1.get())

