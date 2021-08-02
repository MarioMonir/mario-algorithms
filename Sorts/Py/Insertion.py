#!/usr/bin/python
import time as tm
import random

print("give me a bottle of rum!")


def insertion_sort(l):
    for j in range(0, len(l)):
       key = l[j]
       i = j-1
       while i >= 0 and l[i] > key:
           l[i+1] = l[i]
           i = i-1
       l[i+1] = key  


l = random.sample(range(25), 25)
l1 = l.copy()
l2 = l.copy()

print(l1)
st1 = tm.time()
insertion_sort(l1)
print("%s seconds " % (tm.time() - st1))
print(l1)


print(l2)
st2 = tm.time() 
l2.sort()
print("%s seconds " % (tm.time() - st2))
print(l2)



