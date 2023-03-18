def sift_down(data, i, swaps):
    """Sift down the element at index i in the data list to maintain heap property."""
    n = len(data)
    min_index = i
    l = 2 * i + 1
    if l < n and data[l] < data[min_index]:
        min_index = l
    r = 2 * i + 2
    if r < n and data[r] < data[min_index]:
        min_index = r
    if i != min_index:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(data, min_index, swaps)


def build_heap(data):
    """Build a min-heap from the given data list using O(n) swaps."""
    swaps = []
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(data, i, swaps)
    return swaps


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    swaps = build_heap(data)
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])
