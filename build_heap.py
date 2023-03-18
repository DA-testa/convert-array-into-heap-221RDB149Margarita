def heapify(arr, n, i, swaps):
  
    largest = i 
    l = 2 * i + 1 
    r = 2 * i + 2  
 

    if l < n and arr[l] > arr[largest]:
        largest = l
 

    if r < n and arr[r] > arr[largest]:
        largest = r
 

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        swaps.append((i, largest))
 
  
        heapify(arr, n, largest, swaps)
 
 
def heapSort(arr):
    n = len(arr)
    swaps = []
 

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, swaps)
 

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        swaps.append((0, i))
        heapify(arr, i, 0, swaps)
 
    return swaps
 
 

n = int(input())
arr = list(map(int, input().split()))

swaps = heapSort(arr)

print(len(swaps))
print()
for s in swaps:
    print(s[0], s[1])
