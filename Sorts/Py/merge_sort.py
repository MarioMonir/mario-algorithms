#!/usr/bin/python
import random
import time as tm


def mergeSort(arr): 
    if len(arr) > 1:
        mid = len(arr)//2 
        l = arr[:mid] 
        r = arr[mid:] 
  
        mergeSort(l) 
        mergeSort(r)  
  
        i = j = k = 0
        
        while i < len(l) and j < len(r): 
            if l[i] < r[j]: 
                arr[k] = l[i] 
                i += 1
            else: 
                arr[k] = r[j] 
                j += 1
            k += 1
          
        while i < len(l): 
            arr[k] = l[i] 
            i += 1
            k += 1
          
        while j < len(r): 
            arr[k] = r[j] 
            j += 1
            k += 1


def print_list( arr ):
    for i in range(len(arr)):         
        print(arr[i], end=" ")
    print() 


arr = random.sample(range(25), 25)
print(arr)
st1 = tm.time()
mergeSort(arr)
print("%s seconds " % (tm.time() - st1))
print(arr)


