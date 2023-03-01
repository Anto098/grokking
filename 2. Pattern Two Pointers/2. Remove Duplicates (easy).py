def remove_duplicates(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i+1]:
            arr.pop(i+1)
        else:
            i += 1

    return len(arr)


if __name__ == "__main__":
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
