import math


class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    start, end = 0, 1
    while reader.get(end) < key:
        new_start = end + 1
        end += (end - start + 1) * 2
        start = new_start
    return binary_search(reader, key, start, end)


def binary_search(reader, key, start, end):
    print(f"{reader.arr=}, {key=}, {start=} ({reader.arr[start]}), {end=}")
    while start <= end:
        mid = start + (end - start) // 2
        r = reader.get(mid)
        if r == key:
            return mid
        elif r > key:
            end = mid - 1
        else:
            start = mid + 1

    return -1


if __name__ == "__main__":
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))
