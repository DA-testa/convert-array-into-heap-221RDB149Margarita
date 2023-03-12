# python3

def heapify(arr, n, i, swaps):
    """
    Heapify subtree rooted at index i.
    """
    
    l = 2 * i + 1
    r = 2 * i + 2 

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        swaps.append((i, largest))
        arr[i], arr[largest] = arr[largest], arr[i] 

        heapify(arr, n, largest, swaps)

def build_heap(arr):
    swaps = []
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, swaps)

    return swaps

def main():
    source = input()
    if "F" in source:
        filename = input()
        with open("tests/" + filename, 'r', encoding = "utf-8") as f:
            n = int(f.readline())
            arr = list(map(int, f.readline().split()))
    elif "I" in source:
        n = int(input())
        arr = list(map(int, input().split()))
    else:
        exit()
    assert len(arr) == n
    swaps = build_heap(arr)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()