import math
import random as r
import time as tm

class Heap:
    @staticmethod
    def max_heapify(arr, n, i):
        left = (2*i)+1
        right = (2*i)+2

        if left < n and arr[left] > arr[i]:
            largest = left
        else:
            largest = i
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            return Heap.max_heapify(arr, n, largest)

    @staticmethod
    def build_max_heap(arr, n):
        for i in range(math.floor(n/2)-1, -1, -1):
            Heap.max_heapify(arr, n, i)
        return arr

    @staticmethod
    def heap_sort(arr):
        n = len(arr)
        for i in range(n, 0, -1):
            Heap.build_max_heap(arr, i)
            arr[0], arr[i-1] = arr[i-1], arr[0]
        return arr
# ===========================================================


arr = r.sample(range(25), 25)


print(arr)
st1 = tm.time()
Heap.heap_sort(arr)
print("%s seconds " % (tm.time() - st1))
print(arr)

