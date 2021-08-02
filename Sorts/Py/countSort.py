import random
import time as tm


def counting_sort(arr):
    largest = max(arr)
    arr.insert(0, None)
    
    # fill array cnt by zeros 
    cnt = [0]*(largest+1)

    # declare srt array (sorted array will be returned)
    srt = [None]*(len(arr))
    
    # now array cnt contain the number of elements in the given array arr
    for i in range(1,len(arr)):
        cnt[arr[i]] += 1

    for i in range(1, largest+1):
        cnt[i] = cnt[i] + cnt[i - 1] 
     
 
    for i in range(len(arr)-1, 0, -1):
        srt[cnt[arr[i]]]=arr[i]
        cnt[arr[i]]-=1  
     
    arr.pop(0)
    srt.pop(0)     

    return srt

# =======================================


arr = random.sample(range(25), 25)
print(arr)
st1 = tm.time()
arr = counting_sort(arr)
print("%s seconds " % (tm.time() - st1))
print(arr)

# sort         =  4.291534423828125e-06 seconds
# count        =  3.24249267578125e-05 seconds
# insertion    =  5.078315734863281e-05 seconds
# merge        =  8.869171142578125e-05 seconds
# heap         =  0.00036406517028808594 seconds

