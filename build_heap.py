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
try:
 text = input().strip()
        if "I" in text:
            n = int(input())
            arr = list(map(int, input().split()))
        elif "F" in text:
            filename = input()
            with open ("tests/" + filename, 'r') as f:
                n = int(f.readline())
                arr = list(map(int,f.readline().split()))
        else:
            raise ValueError("Invalid input, please input F or I!")
        if n != len(arr):
            raise ValueError("Invalid input, length of data does not match!")
        swaps = heapSort(arr)
        print(len(swaps))
        print()
        for s in swaps:
          print(s[0], s[1]))
   
    except ValueError:
        print("Error")



