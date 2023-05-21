def search_ceiling_of_a_number(arr, key):
    start = 0
    end = len(arr) - 1
    mid = start + (end - start) // 2
    while start <= end:
        if arr[mid] == key:
            return mid

        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

        mid = start + (end - start) // 2

    return mid + 1 if mid + 1 < len(arr) else -1


if __name__ == "__main__":
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))
