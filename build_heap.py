def parent(i):
    return (i-1)//2

def left_child(i):
    return 2*i + 1

def right_child(i):
    return 2*i + 2

def sift_down(i, arr, swaps):
    min_idx = i
    l = left_child(i)
    if l < len(arr) and arr[l] < arr[min_idx]:
        min_idx = l
    r = right_child(i)
    if r < len(arr) and arr[r] < arr[min_idx]:
        min_idx = r
    if i != min_idx:
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps.append((i, min_idx))
        sift_down(min_idx, arr, swaps)

def build_heap(arr):
    swaps = []
    for i in range(len(arr)//2, -1, -1):
        sift_down(i, arr, swaps)
    return swaps

n = int(input())
arr = list(map(int, input().split()))
swaps = build_heap(arr)

print(len(swaps))
for i, j in swaps:
    print(i, j)
