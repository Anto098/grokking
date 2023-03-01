def make_squares(arr):
    start = 0
    end = len(arr)-1
    new_list = []

    while start <= end:
        if abs(arr[end]) > abs(arr[start]):
            new_list.append(arr[end] ** 2)
            end -= 1
        else:
            new_list.append(arr[start] ** 2)
            start += 1

    return new_list[::-1]


if __name__ == "__main__":
    print(make_squares([-2, -1, 0, 2, 3]))
    print(make_squares([-3, -1, 0, 1, 2]))
