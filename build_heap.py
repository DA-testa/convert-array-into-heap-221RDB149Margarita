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


def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        heapify(data, n, i, swaps)
    return swaps


def main():
    input_method = input()

    if 'I' in input_method:
        n = int(input())
        data = list(map(int, input().split()))
    elif 'F' in input_method:
        filename = input()
        if 'a' in filename:
            print("Invalid filename")
            return
        with open("tests/" + filename, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        print("Invalid input method")
        return

    assert n >= 1 and n <= 100000
    assert len(data) == n
    assert all(0 <= data[i] <= 10**9 for i in range(n))

    swaps = build_heap(data)

    for i in range(n):
        left_child = 2*i + 1
        right_child = 2*i + 2
        if left_child < n:
            assert data[i] >= data[left_child]
        if right_child < n:
            assert data[i] >= data[right_child]

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
