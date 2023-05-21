def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    order = "ASC" if arr[end] - arr[start] > 0 else "DESC"
    mid = start + (end - start) // 2
    while start <= end:
        if arr[mid] == key:
            return mid
        if key < arr[mid]:
            if order == "ASC":
                end = mid - 1
            else:
                start = mid + 1
        else:
            if order == "ASC":
                start = mid + 1
            else:
                end = mid - 1

        mid = start + int((end - start) / 2)

    return -1


if __name__ == "__main__":
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))
