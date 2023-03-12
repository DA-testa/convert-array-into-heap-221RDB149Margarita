# python3

import math

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        min_index = i
        if 2 * i + 1 < n and data[2 * i + 1] < data[min_index]:
            min_index = 2 * i + 1
        if 2 * i + 2 < n and data[2 * i + 2] < data[min_index]:
            min_index = 2 * i + 2
        if i != min_index:
            swaps.append((i, min_index))
            data[i], data[min_index] = data[min_index], data[i]
            j = min_index
            while j <= (n//2-1):
                k = j
                if 2 * j + 1 < n and data[2 * j + 1] < data[k]:
                    k = 2*j+1
                if 2 * j + 2 < n and data[2 * j + 2] < data[k]:
                    k = 2 * j + 2
                if j != k:
                    swaps.append((j, k))
                    data[j], data[k] = data[k], data[j]
                    j = k
                else:
                    break

    return swaps

def main():
    source = input()
    if "F" in source:
        filename = input()
        with open("tests/" + filename, 'r', encoding = "utf-8") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    elif "I" in source:
        n = int(input())
        data = list(map(int, input().split()))
    else: 
        print("Invalid input source.")
        exit()

    if data != sorted(data):
        swaps = build_heap(data)

        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    else:
        print("Data is already a heap.")

if __name__ == "__main__":
    main()