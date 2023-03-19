class MinHeap:
    def __init__(self, arr):
        self.arr = arr
        self.swaps = []
        self.build_heap()

    def build_heap(self):
        n = len(self.arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < len(self.arr) and self.arr[left] < self.arr[smallest]:
            smallest = left

        if right < len(self.arr) and self.arr[right] < self.arr[smallest]:
            smallest = right

        if smallest != i:
            self.swaps.append((i, smallest))
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.heapify(smallest)

    def print_swaps(self):
        print(len(self.swaps))
        for x in self.swaps:
            print(*x)

if __name__ == "__main__":
    source = input("source: ").strip().upper()

    if source == "I":
        n = int(input())
        arr = list(map(int, input().split()))
    elif source == "F":
        filename = input("file name: ").strip()

        assert filename.endswith(".a")

        with open("tests/" + filename, "r") as file:
            n = int(file.readline())
            arr = list(map(int, file.readline().split()))
    else:
        raise ValueError("Invalid source")


    assert len(arr) == n

    min_heap = MinHeap(arr)
    min_heap.print_swaps()
