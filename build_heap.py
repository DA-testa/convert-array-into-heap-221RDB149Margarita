def sift_down(n, arr, swaps):
    i = 0
    while 2*i+1 < n:
        j = i
        if arr[2*i+1] < arr[j]:
            j = 2*i+1
        if 2*i+2 < n and arr[2*i+2] < arr[j]:
            j = 2*i+2
        if i != j:
            swaps.append((i, j))
            arr[i], arr[j] = arr[j], arr[i]
            i = j
        else:
            break

def build_heap(n, arr):
    swaps = []
    for i in range(n//2, -1, -1):
        sift_down(n, arr, swaps, i)
    return swaps

n = int(input())
arr = list(map(int, input().split()))
swaps = build_heap(n, arr)

print(len(swaps))
for i, j in swaps:
    print(i, j)
